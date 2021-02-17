import sys
sys.path.append("../")

from app.app import app
from flask import request
from bson import json_util
from app.helpers.mongoConnection import *



@app.route("/celebrity/create")
def create_celebrity():
    celeb = request.args
    
    id_ = insert_celebrity(**celeb)
    return json_util.dumps(id_)