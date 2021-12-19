from pymongo import MongoClient


cluster =MongoClient("mongodb+srv://<username>:<password>@cluster0.l8x9e.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=cluster['news_aggregator']
collection=db['news']