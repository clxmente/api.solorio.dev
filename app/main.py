from fastapi import FastAPI, Request
from starlette.responses import JSONResponse, RedirectResponse
from app.routers.exceptions import DoesNotExist

from app.routers.exceptions import PasswordNotLongEnough, PasswordTooLong, ExcludedAllSets

# import the routers from other modules
from app.routers.nba import nba
from app.routers.password import password

app = FastAPI(
    title="api.solorio.dev",
    description="Personal API built for my projects 🚀",
    version="1.0.0"
)

app.include_router(nba.router)
app.include_router(password.router)

@app.exception_handler(DoesNotExist)
async def player_dne(request: Request, exc: DoesNotExist):
    return JSONResponse(
        status_code=404,
        content={
            "message": "No record found."
        }
    )

# Exception Handlers
@app.exception_handler(PasswordNotLongEnough)
async def length_handler(request: Request, exc: PasswordNotLongEnough):
    return JSONResponse(
        status_code=400,
        content={
            "length": exc.length,
            "message": "Please choose a password of at least 8 characters."
        }
    )

@app.exception_handler(PasswordTooLong)
async def length_too_long(request: Request, exc: PasswordTooLong):
    return JSONResponse(
        status_code=400,
        content={
            "length": exc.length,
            "message": "Please choose a password length under 64 characters ☹️",
        }
    )

@app.exception_handler(ExcludedAllSets)
async def no_sets_selected(request: Request, exc: ExcludedAllSets):
    return JSONResponse(
        status_code=400,
        content={
            "message": "Please select at least one character set."
        }
    )

@app.get("/", response_class=RedirectResponse)
async def redirect_to_docs():
    return RedirectResponse("/docs")

@app.get("/ping")
async def ping():
    return {"messsage": "hello!"}