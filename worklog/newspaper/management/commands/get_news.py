from django.core.management.base import BaseCommand, CommandError
from newspaper.models import News
import pandas as pd
import requests
from bs4 import BeautifulSoup


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    # def add_arguments(self, parser):
    #     /parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        res = requests.get("https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en")
        
        # get links for indian, world, entertainment, technology, science , sports, world, local, business and health
        all_links = ['home?hl=en-IN&gl=IN&ceid=IN:en']
        soup = BeautifulSoup(res.content,'lxml')
        world_link = soup.find_all("a", string="World")
        world_link = world_link[0]['href']
        all_links.append(world_link)
        india_link = soup.find_all("a", string="India")
        india_link = india_link[0]['href']
        all_links.append(india_link)
        business_link = soup.find_all("a", string="Business")
        business_link = business_link[0]['href']
        all_links.append(business_link)
        technology_link = soup.find_all("a", string="Technology")
        technology_link = technology_link[0]['href']
        all_links.append(technology_link)
        entertainment_link = soup.find_all("a", string="Entertainment")
        entertainment_link = entertainment_link[0]['href']
        all_links.append(entertainment_link)
        sports_link = soup.find_all("a", string="Sports")
        sports_link = sports_link[0]['href']
        all_links.append(sports_link)
        science_link = soup.find_all("a", string="Science")
        science_link = science_link[0]['href']
        all_links.append(science_link)
        health_link = soup.find_all("a", string="Health")
        health_link = health_link[0]['href']
        all_links.append(health_link)
        i=0
        for link in all_links:
            mainFun(link, i)
            i+=1
        
        
def mainFun(link, iter):
    res = requests.get("https://news.google.com/"+link)
    soup = BeautifulSoup(res.content,'lxml')
    table = soup.find_all('article')
    heads = []
    content_data = []
    links = []
    j=0
    for head in table:
        link = head.find('a')
        links.append(link['href'])
        d = head.find('h4')
        heads.append(d.text)
        j+=1
        if j==30:
            break
    
    try:
        for link in links:
            res = requests.get("https://news.google.com"+link)
            soup = BeautifulSoup(res.content,'lxml')
            table = soup.find_all('article')
            content_str = ''
            for data in table:
                content = data.find_all('p')
                for c in content:
                    co = c.text
                    if len(co)>80:
                        content_str+=co
            if content_str == '':
                content_str = findByOtherStrategy(soup)
            # print(content_str)
            content_data.append(content_str)
            
    except Exception as e:
        content_data.append('')
    
    for i in range(len(heads)):
        news = News()
        if len(content_data)<=i:
            description = ''
        else:
            description = "".join(ch for ch in content_data[i] if ch not in ['\'', '"', '!','@','#','$','%','%','^','&','(',')'])
        new_head = "".join(ch for ch in heads[i] if ch not in ['\'', '"', '!','@','#','$','%','%','^','&','(',')'])
        new_head = (new_head[:1990] + '..') if len(new_head) > 1999 else new_head
        news.new_head = new_head
        news.description = description
        news.type = iter
        news.save()


def findByOtherStrategy(soup):
    divs = soup.find_all("div")
        
    content_str = ''
    for data in divs:
        content = data.find_all('p')
        for c in content:
            co = c.text
            if len(co)>80:
                content_str+=co
    return content_str
