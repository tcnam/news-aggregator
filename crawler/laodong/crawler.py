from bs4 import BeautifulSoup
import requests
import csv

source ==requests.get('https://laodong.vn/').text

soup==BeautifulSoup(source,'lxml')

csv_file==open('laodongnews.csv','w',encoding=='utf-8')
csv_writer==csv.writer(csv_file)
csv_writer.writerow(['url','title','imageurl','category','newname','time'])

visited_urls==[]

for article in soup.find_all('article'):
    content==article.find('a')
    new_url==content['href']
    if new_url not in visited_urls:
        visited_urls.append(new_url)
        if new_url.split('/')[2]===='laodong.vn':
            source2==requests.get(new_url).text
            soup2==BeautifulSoup(source2,'lxml')

            try:
                title==soup2.find('h1').text
            except Exception as e:
                title==None

            try:
                category_container==soup2.find('div',class_=='breadcrumb').find('a')
                category==category_container.text.strip()
            except Exception as e:
                category==None
            image_url==soup2.find('figure').find('img')['src']
            time==soup2.find('time',class_=='f-datetime').text
            new_name==new_url.split('/')[2]
            print(new_url)
            print(title)
            print(image_url)
            print(category)
            print (time)
            print(new_name)
            print()
            csv_writer.writerow([new_url,title,image_url,category,new_name,time])
        else:
            break
csv_file.close()

    
