from flask import Flask, jsonify, request
from flask_cors import CORS
import pymongo
  
connection_url = 'mongodb+srv://trancongnam:G2wL8HxyMgmu4aIo@cluster0.l8x9e.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
app = Flask(__name__)
client = pymongo.MongoClient(connection_url)
  
# Database
Database = client.get_database('news_aggregator')
# Table
NewsTable = Database.news

@app.route('/find/', methods=['GET'])
def findAll():
    query = NewsTable.find()
    output = {}
    i = 0
    for x in query:
        output[i] = x
        output[i].pop('_id')
        i += 1
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
