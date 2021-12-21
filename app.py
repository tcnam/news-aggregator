from dotenv import load_dotenv
import json
import os
from bson import json_util
from flask import Flask, request, Response
import pymongo



load_dotenv() # use dotenv to hide sensitive credential as environment variables
connection_url=os.environ.get("url")
client = pymongo.MongoClient(connection_url)
# Database
db = client.get_database('news_aggregator')

app = Flask(__name__)

def CategoryNormalize(category):
    switcher={
        'yte':'Y tế',
        'xahoi':'Xã hội',
        'video':'Video',
        'moitruong':'Môi trường',
        'kinhdoanh':'Kinh doanh',
        'phapluat':'Pháp luật',
        'thegioi':'Thế giới',
        'giaoduc':'Giáo dục',
    }
    return switcher.get(category)
@app.route('/')
def helloworld():
    return 'hello world'
@app.route('/news/', methods=['GET'])
def findAll():
    news=[]
    for new in db.news.find():
        news.append(new)
    return Response(
        json.dumps(news,default=json_util.default),
        mimetype="application/json",
        status=200,
    )
@app.route('/news/<categoryvalue>/',methods=['GET'])
def findNewsBasedOnCategory(categoryvalue):
    catevalue=CategoryNormalize(categoryvalue)
    news=[]
    for result in db.news.find({'category':catevalue}).limit(5):
        news.append(result)
    return Response(
        json.dumps(news,default=json_util.default),
        mimetype="application/json",
        status=200,
    )
    
    
if __name__ == '__main__':
    app.run()

