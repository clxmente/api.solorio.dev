from fastapi import APIRouter

from pydantic import BaseModel
from app.routers.nba.query_mongo import return_player_info

class NBAPlayerResponse(BaseModel):
    NBA_ID: int
    FULL_NAME: str
    JERSEY_NUM: str
    POS: str
    TEAM: str

class Message(BaseModel):
    message: str

router = APIRouter(
    prefix="/nba",
    tags=["NBA"]
)

@router.get(
    "/player/{player_name}", # endpoint,
    description="Get basic player information from an NBA player",
    response_model=NBAPlayerResponse, # how the successful response looks
    responses={404: {"model": Message}})
async def player_endpoint(player_name: str):
    return return_player_info(player_name.replace("-", " "))