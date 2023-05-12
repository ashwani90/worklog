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
        
        soup = BeautifulSoup(res.content,'lxml')
        table = soup.find_all('article')
        heads = []
        content_data = []
        links = []
        for head in table:
            link = head.find('a')
            links.append(link['href'])
            d = head.find('h4')
            heads.append(d.text)
        
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
                content_data.append(content_str)
        except Exception as e:
            content_data.append('')
        
        # for i in range(len(heads)):
        #     news = News()
        #     if len(content_data)<i:
        #         description = ''
        #     else:
        #         description = "".join(ch for ch in content_data[i] if ch not in ['\'', '"', '!','@','#','$','%','%','^','&','(',')'])
        #     new_head = "".join(ch for ch in heads[i] if ch not in ['\'', '"', '!','@','#','$','%','%','^','&','(',')'])
        #     new_head = (new_head[:1990] + '..') if len(new_head) > 1999 else new_head
        #     news.new_head = new_head
        #     news.description = description
        #     news.save()
        # for data in table:
        #     print(data)
        self.stdout.write(
            self.style.SUCCESS('Successfully closed poll')
        )

def findByOtherStrategy(soup):
    mydivs = soup.select("div.storyParagraphFigure")
    content_str = ''
    print(mydivs);
    for data in mydivs:
        content = data.find_all('p')
        for c in content:
            co = c.text
            if len(co)>80:
                content_str+=co
    return content_str
