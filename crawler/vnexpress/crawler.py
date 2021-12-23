from bs4 import BeautifulSoup
import requests
import csv

def extract_sitemaps(sitemap_url):
    res = requests.get(sitemap_url)
    if res.status_code != 200:
        return []

    soup = BeautifulSoup(res.text, 'xml')

    sitemap_tags = soup.find_all('sitemap')

    sitemaps = []
    for sitemap in sitemap_tags:
        loc = sitemap.find('loc')
        sitemaps.append(loc.text)
    return sitemaps

def extract_urls_from_sitemap(sitemap_url):
    res = requests.get(sitemap_url)
    if res.status_code != 200:
        return []

    soup = BeautifulSoup(res.text, 'xml')

    urls = []
    url_tags = soup.find_all('url')
    for url in url_tags:
        loc = url.find('loc')
        urls.append(loc.text)

    return urls

def extract_text_from_url(url):
    res = requests.get(url)
    if res.status_code != 200:
        return ''

    soup = BeautifulSoup(res.text, 'html.parser')

    h1 = soup.find('h1', class_='title_news_detail mb10')
    h2 = soup.find('h2', class_='description')
    if (h1 is None) or (h2 is None):
        return ''

    chunks = []
    chunks.append(h1.get_text().strip())
    chunks.append(h2.get_text().strip())

    main_content = soup.find_all('p', class_='Normal')
    for p in main_content[:2]:
        if p.find('a') is None:
            chunks.append(p.get_text().strip())

    return '\n'.join(chunks)

visited_urls=[]
sitemap_url='https://vnexpress.net/sitemap/1000000/sitemap.xml'
sitemaps=extract_sitemaps(sitemap_url)
for sitemap in sitemaps[:2]:
    urls=extract_urls_from_sitemap(sitemap)
    for url in urls[:50]:
        if url not in visited_urls:
            visited_urls.add(url)
            text=extract_text_from_url(url)
            print(text)

#csv_file=open('vnexpressnews.csv','w',encoding='utf-8')
#csv_writer=csv.writer(csv_file)
#csv_writer.writerow(['url','title','imageurl','category','newname','time'])

#csv_file.close()

    
