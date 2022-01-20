from typing import Optional
from fastapi import APIRouter
from pydantic import BaseModel

from app.routers.password.password_funcs import gen_password
from app.routers.exceptions import PasswordNotLongEnough, PasswordTooLong

# Models
class PasswordOutput(BaseModel):
    length: Optional[int] = 10
    password: str

class Message(BaseModel):
    message: str

router = APIRouter(
    tags=["Password Generator"]
)

# Paths
@router.get(
    "/password", 
    response_model=PasswordOutput, 
    responses={400: {"model": Message}}
)
async def password_endpoint(length: int = 10, exclude: Optional[str] = None):
    """ 
    Generate a password with a given length (default 10).

    Can exclude certain character sets with the optional `exclude` parameter:
    - **special**
    - **digits**
    - **upper**
    - **lower**

    Example: `/password?exclude="special,upper"` to exclude special characters
    and uppercase characters.
    """
    if (length < 8):
        raise PasswordNotLongEnough(length)
    elif (length > 64):
        raise PasswordTooLong(length)
    output = gen_password(length, exclude)
    return {
        "length": length,
        "password": output
    }