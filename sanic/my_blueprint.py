# ./my_blueprint.py
import time

import asyncio
from sanic import Blueprint
from sanic.response import json


bp = Blueprint("my_blueprint")


@bp.route("/")
async def bp_root(request):
    return json({"my": "blueprint"})


@bp.route("/somedata")
async def bp_somedate(request):
    await asyncio.sleep(10)
    return json(list(range(100)))
