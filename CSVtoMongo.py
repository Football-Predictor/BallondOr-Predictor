from pymongo import MongoClient
import pandas as pd

def addCSVToMongoDB(csvPath, connectionString, collectionName="BallondOrPredictor",dbName="FootballPredictor"):
    """Adds csv data to a mongoDB database"""
    client = MongoClient(connectionString)
    db = client[dbName]
    collection = db[collectionName]
    df = pd.read_csv(csvPath)
    data = df.to_dict(orient='records')
    collection.insert_many(data)


def clearMongoDB(connectionString, collectionName="BallondOrPredictor",dbName="FootballPredictor"):
    """Clears a mongoDB database"""
    client = MongoClient(connectionString)
    db = client[dbName]
    collection = db[collectionName]
    collection.delete_many({})