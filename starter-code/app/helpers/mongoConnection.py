from pymongo import MongoClient

client = MongoClient()

celebrities = client.labflask_toni.celebrities
movies = client.labflask_toni.movies

def insert_celebrity(**celeb):
    res = celebrities.insert_one(celeb)
    return res.inserted_id


def fetch_celebrity(**celeb):
    res = celebrities.find({"name":celeb}, {"name":1, "occupation":1, "catch_phrase":1  ,"_id":0})
    return list(res)