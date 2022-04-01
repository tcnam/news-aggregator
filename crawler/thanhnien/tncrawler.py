from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime

def extractMainUrls(site_url):
    site_urls=[]
    source = requests.get(site_url).text
    soup=BeautifulSoup(source,'lxml')
    menu_categories=soup.find_all('a',class_='menu-parent')
    for menu_category in menu_categories:
        if len(menu_category['href'].split('/'))==5:
            site_urls.append(menu_category['href'])
    return site_urls;

def getAllUrlsThanhNien():
    csv_file=open('news.csv','w',encoding='utf-8')
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(['url','title','imageurl','category','newname','time'])

    visited_urls=[]
    main_url='https://thanhnien.vn/'
    print(len(main_url.split('/')))

    site_urls=extractMainUrls(main_url)
    print(site_urls)

    for site_url in site_urls:
        source = requests.get(site_url).text
        soup=BeautifulSoup(source,'lxml')
        for article in soup.find_all('article'):
            content=article.find('a')
            new_url=content['href']
            if new_url not in visited_urls:
                visited_urls.append(new_url)
                if new_url.split('/')[2]=='thanhnien.vn':
                    source2=requests.get(new_url).text
                    soup2=BeautifulSoup(source2,'lxml')

                    try:
                        title=soup2.find('h1',class_='details__headline cms-title').text.strip()
                    except Exception as e:
                        title='Null'

                    try:
                        category_container=soup2.find('div',class_='breadcrumbs').find_all('a')
                        category='Null'
                        for temp in category_container:
                            content=temp['href']
                            if(len(content.split('/'))==5):
                                category=temp.text.strip()   
                    except Exception as e:
                        category='Null'

                    try: 
                        image_url=soup2.find('img',class_='cms-photo')['src']
                    except:
                        image_url='Null'
                    time=soup2.find('time').text
                    time=datetime.strptime(time, '%H:%M - %d/%m/%Y')
                    new_name=new_url.split('/')[2]

                    if category!='Video':
                        print(new_url)
                        print(title)
                        print(category)
                        print(image_url)
                        print (time)
                        print(new_name)
                        print()
                        csv_writer.writerow([new_url,title,image_url,category,new_name,time])

    csv_file.close()

getAllUrlsThanhNien()
#for site_url in site_urls:


    
