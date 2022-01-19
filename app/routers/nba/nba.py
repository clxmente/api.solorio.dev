from fastapi import APIRouter
from typing import List

from pydantic import BaseModel
from app.routers.nba.query_mongo import return_player_info, return_team_info

class NBAPlayerResponse(BaseModel):
    NBA_ID = 2544
    FULL_NAME = "LeBron James"
    JERSEY_NUM = "6"
    POS = "F"
    TEAM = "LAL"

class NBATeamPlayersModel(BaseModel):
    FULL_NAME = "Anthony Davis"
    JERSEY_NUM = "3"
    POS = "F-C"

class NBATeamResponse(BaseModel):
    __root__: List[NBATeamPlayersModel]

class Message(BaseModel):
    message: str

router = APIRouter(
    prefix="/nba",
    tags=["NBA"]
)

@router.get(
    "/player/{player_name}", # endpoint,
    description="Get basic player information from an NBA player.",
    response_model=NBAPlayerResponse, # how the successful response looks
    responses={404: {"model": Message}}
)
async def player_endpoint(player_name: str):
    return return_player_info(player_name.replace("-", " "))

@router.get(
    "/team/{team_abbreviation}",
    description="Get the list of players on an NBA team.",
    response_model=NBATeamResponse,
    responses={404: {"model": Message}}
)
async def team_endpoint(team_abbreviation: str):
    return return_team_info(team_abbreviation)