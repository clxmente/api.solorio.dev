from fastapi import APIRouter
from app.routers.nba.query_mongo import return_player_info

router = APIRouter(
    prefix="/nba",
    tags=["NBA"]
)

@router.get("/players")
async def player_endpoint(player_name: str):
    return return_player_info(player_name.replace("-", " "))