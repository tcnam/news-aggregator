from bs4 import BeautifulSoup
import requests
import csv

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

csv_file=open('thanhniennews.csv','w',encoding='utf-8')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['url','title','imageurl','category','newname','time'])

visited_urls=[]
site_url='https://thanhnien.vn/'
print(len(site_url.split('/')))
'''
test_url='https://thanhnien.vn/tai-chinh-kinh-doanh/'
if len(test_url.split('/'))==5:
    print ("True")
else:
    print("False")
'''

source = requests.get(site_url).text
soup=BeautifulSoup(source,'lxml')
trending=soup.find('div',class_='tab-pane fade')
#print(trending)
articletrendings=trending.find_all('article',class_='story--text')
for article in articletrendings:
    content=article.find('a')
    new_url=content['href']
    if new_url not in visited_urls:
        visited_urls.append(new_url)
        if new_url.split('/')[2]=='thanhnien.vn':
            source2=requests.get(new_url).text
            soup2=BeautifulSoup(source2,'lxml')
            try:
                title=soup2.find('h2',class_='details__headline cms-title').text.strip()
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
            image_url=soup2.find('td',class_='pic').find('img')['src']
            time=soup2.find('time').text
            new_name=new_url.split('/')[2]
            print(new_url)
            print(title)
            print(category)
            print(image_url)
            print (time)
            print(new_name)
            print()
            csv_writer.writerow([new_url,title,image_url,category,new_name,time])
"""
for article in soup.find_all('article'):
    content=article.find('a')
    new_url=content['href']
    if new_url not in visited_urls:
        visited_urls.append(new_url)
        if new_url.split('/')[2]=='thanhnien.vn':
            source2=requests.get(new_url).text
            soup2=BeautifulSoup(source2,'lxml')
            try:
                title=soup2.find('h1').text
            except Exception as e:
                title=None
            try:
                category_container=soup2.find('div',class_='breadcrumb').find('a')
                category=category_container.text.strip()
                if(category=='Văn hóa - Giải trí'):
                    category='Giải trí'  
            except Exception as e:
                category=None
            image_url=soup2.find('figure').find('img')['src']
            time=soup2.find('time',class_='f-datetime').text
            new_name=new_url.split('/')[2]
            print(new_url)
            print(title)
            print(image_url)
            print(category)
            print (time)
            print(new_name)
            print()
            csv_writer.writerow([new_url,title,image_url,category,new_name,time])
                
            
"""

csv_file.close()
#for site_url in site_urls:


    
