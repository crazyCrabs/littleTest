# ./my_blueprint.py
import asyncio
import imp
import time


from sanic import Blueprint
from sanic.response import json, text
from sanic_ext import openapi


bp = Blueprint("my_blueprint")


@bp.reload_process_start
async def reload_start(*_):
    print(">>>>>> reload_start <<<<<<")


@bp.main_process_start
async def main_start(*_):
    print(">>>>>> main_start <<<<<<")


@bp.middleware("request")
async def add_key(request):
    # Arbitrary data may be stored in request context:
    request.ctx.foo = "bar"


@bp.middleware("response")
async def custom_banner(request, response):
    response.headers["Server"] = "Fake-Server"


@bp.middleware("response")
async def prevent_xss(request, response):
    response.headers["x-xss-protection"] = "1; mode=block"


@bp.route("/")
@openapi.summary("This is a summary")
@openapi.description("This is a description")
async def bp_root(request, name='foo'):
    """This is a simple foo handler

    Now we will add some more details

    openapi:
    ---
    operationId: fooDots
    tags:
      - one
      - two
    parameters:
      - name: limit
        in: query
        description: How many items to return at one time (max 100)
        required: false
        schema:
          type: integer
          format: int32
    responses:
      '200':
        description: Just some dots
    """
    res = {"my": "blueprint", "request_id": request.id, "info": request.ctx.foo}
    res.update({
            "effective host": request.host,
            "host header": request.headers.get("host"),
            "forwarded host": request.forwarded.get("host"),
            # "you are here": request.url_for("foo"),
        })
    return json(res)


@bp.route("/somedata/<times:int>")
async def bp_somedate(request, times: int):
    await asyncio.sleep(times)
    return json(list(range(100)))
