
import pymongo
import pandas as pd
import csv
from crawler.laodong.ldcrawler import getAllUrlsLaoDong
from crawler.thanhnien.tncrawler import getAllUrlsThanhNien

def getVisitedUrl():
    CONNECTION_STRING='mongodb+srv://namtran:8KVC0EOM2wN5K7jl@cluster0.l8x9e.mongodb.net/test?authSource=admin&replicaSet=atlas-nocnb5-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true'

    client = pymongo.MongoClient(CONNECTION_STRING)
    dbname=client['news_aggregator']
    collection_name=dbname['news']

    csv_file=open('news.csv','w',encoding='utf-8',newline='')
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(['url','title','imageurl','category','newname','time'])

    news_detail=collection_name.find({},{'_id':False})
    news_df=pd.DataFrame(news_detail)
    visited_urls=[]
    #print(news_df)
    for i in news_df.index:
        url=news_df.iloc[i,0]
        visited_urls.append(url)
        title=news_df.iloc[i,1]
        image_url=news_df.iloc[i,2]
        category=news_df.iloc[i,3]
        new_name=news_df.iloc[i,4]
        time=news_df.iloc[i,5]
        csv_writer.writerow([url,title,image_url,category,new_name,time])  
    csv_file.close()
    return visited_urls

visited_urls=getVisitedUrl()
getAllUrlsLaoDong(visited_urls)
getAllUrlsThanhNien(visited_urls)








