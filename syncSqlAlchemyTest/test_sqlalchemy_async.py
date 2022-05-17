import asyncio

from sqlalchemy import text
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine


meta = MetaData()


async def async_main():
    engine = create_async_engine(
        "postgresql+asyncpg://postgres:123456@10.24.8.168/bigquant_service", echo=True,)
    async with engine.begin() as conn:
        await conn.run_sync(meta.drop_all)
        await conn.run_sync(meta.create_all)

    async with engine.connect() as conn:
        result = await conn.execute(text("select * from stocks limit 10;"))
        print(result.fetchall())

    await engine.dispose()

asyncio.run(async_main())
