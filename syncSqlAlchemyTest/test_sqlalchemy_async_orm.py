import asyncio
import imp
from sqlalchemy.orm import backref

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.future import select
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import selectinload, lazyload
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class A(Base):
    __tablename__ = "a"

    id = Column(Integer, primary_key=True)
    data = Column(String)
    create_date = Column(DateTime, server_default=func.now())
    # bs = relationship("B", lazy="dynamic")
    bs = relationship("B")

    # required in order to access columns with server defaults
    # or SQL expression defaults, subsequent to a flush, without
    # triggering an expired load
    __mapper_args__ = {"eager_defaults": True}


class B(Base):
    __tablename__ = "b"
    id = Column(Integer, primary_key=True)
    a_id = Column(ForeignKey("a.id"))
    data = Column(String)


async def async_main():
    engine = create_async_engine(
        "postgresql+asyncpg://postgres:123456@10.24.8.168/bigquant_service",
        echo=False,
    )

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    # expire_on_commit=False will prevent attributes from being expired
    # after commit. 就是在commit之后还可以继续使用对象的值
    # async_session = sessionmaker(
    #     engine, expire_on_commit=False, class_=AsyncSession
    # )

    # create AsyncSession with expire_on_commit=False
    async_session = AsyncSession(engine, expire_on_commit=False)

    async with async_session() as session:
        async with session.begin():
            session.add_all(
                [
                    A(bs=[B(), B()], data="a1"),
                    A(bs=[B()], data="a2"),
                    A(bs=[B(), B()], data="a3"),
                    A(bs=[B(), B(), B(), B()], data="a4"),
                    A(bs=[B(), B(), B(), B(), B()], data="a5"),
                ]
            )

        stmt = select(A).options(selectinload(A.bs))

        result = await session.execute(stmt)

        for a1 in result.scalars():
            print(">>> a: ", a1.data)
            print(f"created at: {a1.create_date}")
            for b1 in a1.bs:
                print(b1.id)

        result = await session.execute(select(A).order_by(A.id))
        print(result.scalars())
        # result.scalars 是一个迭代器,取了就没了
        a1 = result.scalars().first()
        a1.data = "new data"
        await session.commit()
        # access attribute subsequent to commit; this is what
        # expire_on_commit=False allows
        print(a1.data)

        # 测试
        a5 = await session.get(A, 5)
        print(">>> a5 ", a5, a5.data)

    # for AsyncEngine created in function scope, close and
    # clean-up pooled connections
    await engine.dispose()


asyncio.run(async_main())
