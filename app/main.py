from fastapi import FastAPI, Request
from starlette.responses import JSONResponse, RedirectResponse
from app.routers.exceptions import DoesNotExist

# import the routers from other modules
from app.routers.nba import nba

app = FastAPI(
    title="api.solorio.dev",
    description="Personal API built for my projects 🚀",
    version="1.0.0"
)

app.include_router(nba.router)

@app.exception_handler(DoesNotExist)
async def player_dne(request: Request, exc: DoesNotExist):
    return JSONResponse(
        status_code=404,
        content={
            "message": "No record found."
        }
    )

@app.get("/", response_class=RedirectResponse, status_code=302)
async def redirect_to_docs():
    return RedirectResponse("/docs")

@app.get("/ping")
async def ping():
    return {"messsage": "hello!"}