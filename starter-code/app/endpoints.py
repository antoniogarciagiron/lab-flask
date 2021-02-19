import sys
sys.path.append("../")

from app.app import app
from flask import request
from bson import json_util
from app.helpers.mongoConnection import *

def is_valid(input,keywords):
    for key in keywords:
        if key not in input.keys():
            return False, {"Fail":f"Must pass {key}"}
    return True, "OK"


@app.route('/')
def welcome():
    return 'Welcome to the API'


@app.route("/celebrity/create")
def create_celebrity():
    celeb = request.args
    check, msg = is_valid(celeb,["name","occupation", "catch_phrase"])
    if not check:
        return msg
    res = insert_celebrity(**celeb)
    return json_util.dumps(res)


@app.route("/celebrities")
def show_all_celebrities():
    res = fetch_celebrites_list()
    return json_util.dumps(res)


@app.route("/celebrities/details")
def show_celebrity():
    celeb_id = request.args
    check, msg = is_valid(celeb_id,["_id"])
    if not check:
        return msg
    res = fetch_celebrity(**celeb_id)
    return json_util.dumps(res)   