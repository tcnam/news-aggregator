from unittest import result
from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime

def normalizeDatetime(time_str):
    time_str=time_str.split(' ')
    result=time_str[2]+' '+time_str[3]
    return result

def getAllUrlsLaoDong():
    site_urls=[
        'https://laodong.vn/thoi-su/',
        'https://laodong.vn/the-gioi/',
        'https://laodong.vn/xa-hoi/',
        'https://laodong.vn/phap-luat/',
        'https://laodong.vn/kinh-doanh/',
        'https://laodong.vn/the-thao/',
        'https://laodong.vn/suc-khoe/',
        'https://laodong.vn/van-hoa-giai-tri/',
        'https://laodong.vn/giai-tri/'
    ]

    csv_file=open('news.csv','a',encoding='utf-8')
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(['url','title','imageurl','category','newname','time'])

    visited_urls=[]

    for site_url in site_urls:
        source = requests.get(site_url).text
        soup=BeautifulSoup(source,'lxml')
        for article in soup.find_all('article'):
            content=article.find('a')
            new_url=content['href']
            if new_url not in visited_urls:
                visited_urls.append(new_url)
                if new_url.split('/')[2]=='laodong.vn':
                    source2=requests.get(new_url).text
                    soup2=BeautifulSoup(source2,'lxml')
                    try:
                        title=soup2.find('h1').text.strip()
                    except Exception as e:
                        title='Null'

                    try:
                        category_container=soup2.find('a',class_='main-cat-lnk')
                        category=category_container.text.strip()
                        if(category=='Văn hóa - Giải trí'):
                            category='Giải trí'  
                    except Exception as e:
                        category='Null'

                    try:
                        image_url=soup2.find('figure').find('img')['src']
                    except:
                        image_url='Null'

                    try:
                        time=normalizeDatetime(soup2.find('span',class_='time').text.strip())
                        time=datetime.strptime(time, '%d/%m/%Y %H:%M')
                    except Exception as e:
                        time='Null'
                    new_name=new_url.split('/')[2]

                    print(new_url)
                    print(title)
                    print(image_url)
                    print(category)
                    print (time)
                    print(new_name)
                    print()
                    csv_writer.writerow([new_url,title,image_url,category,new_name,time])        

    csv_file.close()

getAllUrlsLaoDong() 
#time_str='Thứ sáu, 01/04/2022 15:02 (GMT+7)'
#time_str_nor=normalizeDatetime('Thứ sáu, 01/04/2022 15:02 (GMT+7)')
#print(time_str_nor)
