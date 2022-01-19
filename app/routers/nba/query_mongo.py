import json

from pymongo import MongoClient
from starlette.responses import JSONResponse
from bson import json_util
from app.routers.exceptions import DoesNotExist

def return_player_info(name: str) -> dict:
    client = MongoClient(host="localhost", port=27017)
    db = client.nba
    result = db.players.find_one(
        {"LOWER_NAME": name.lower()}, # results where LOWER_NAME = name.lower()
        {"_id": 0, "FNAME": 0, "LNAME": 0, "LOWER_NAME": 0} # exclude fields
    )
    if (result):
        # player name is in players collection
        return JSONResponse(
            status_code=200,
            content=json.loads(json_util.dumps(result))
        )
    else: raise DoesNotExist

def return_team_info(name: str) -> dict:
    client = MongoClient(host="localhost", port=27017)
    db = client.nba
    result = db.players.find(
        {"TEAM": name.upper()},
        {"_id": 0, "FNAME": 0, "LNAME": 0, "LOWER_NAME": 0, "TEAM": 0}
    )
    if (result):
        formatted_res = []
        # team name exists
        for player in result:
            formatted_res.append({
                "FULL_NAME": player["FULL_NAME"],
                "JERSEY_NUM": player["JERSEY_NUM"],
                "POS": player["POS"]
            })
        # print(len(formatted_res)) # how many players in team
        return JSONResponse(
            status_code=200,
            content=json.loads(json.dumps(formatted_res))
        )
    else: raise DoesNotExist
