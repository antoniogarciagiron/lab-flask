from pymongo import MongoClient

client = MongoClient()

celebrities = client.labflask_toni.celebrities
movies = client.labflask_toni.movies

def insert_celebrity(**celeb):
    res = celebrities.insert_one(celeb)
    return res.inserted_id


def fetch_celebrity(**celeb_id):
    res = celebrities.find({"_id":celeb_id}, {"name":1, "occupation":1, "catch_phrase":1  ,"_id":0})
    return res


def fetch_celebrites_list():
    res = celebrities.find(celeb, {"name":1, "_id":1})
    return list(res)