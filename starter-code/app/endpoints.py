import sys
sys.path.append("../")

from app.app import app
from flask import request
from bson import json_util
from app.helpers.mongoConnection import *


@app.route("/celebrity/create")
def create_celebrity():
    celeb = request.args   
    res = insert_celebrity(**celeb)
    return json_util.dumps(res)


@app.route("/celebrities")
def show_all_celebrities():
    res = fetch_celebrites_list()
    return json_util.dumps(res)


@app.route("/celebrities/details")
def show_all_celebrities():
    celeb_id = request.args
    res = fetch_celebrity(**celeb_id)
    return json_util.dumps(res)   