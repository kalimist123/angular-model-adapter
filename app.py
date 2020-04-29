from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.responses import Response



_COURSES = [
    {
        "id": 1,
        "code": "adv-maths",
        "name": "Advanced Mathematics",
        "created": "2018-08-14T12:09:45",
    },
    {
        "id": 2,
        "code": "cs1",
        "name": "Computer Science I",
        "created": "2018-06-12T18:34:16",
    },
]

async def homepage(request):
    return JSONResponse(_COURSES)


app = Starlette(routes=[
                    Route('/courses', homepage),
                ])

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_headers=["*"],
        allow_methods=["*"],
        expose_headers=["X-Status"],
        allow_credentials=True,
    )




#@app.route("/courses")
#async def courses_list(req, res):
 #   res.media = _COURSES


#if __name__ == "__main__":
#    app.run()
