import time

from my_blueprint import bp
from sanic import Request, Sanic


class NanoSecondRequest(Request):
    @classmethod
    def generate_id(*_):
        return time.time_ns()


app = Sanic(__name__, request_class=NanoSecondRequest)
app.config.OAS_UI_DEFAULT = 'swagger'
app.blueprint(bp)

app.run(dev=True)
