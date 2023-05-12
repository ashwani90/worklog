from newspaper.models import News
import pandas as pd
import requests
from bs4 import BeautifulSoup

def run():
    res = requests.get("https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en")
    soup = BeautifulSoup(res.content,'lxml')
    table = soup.find_all('h4')[0] 
    df = pd.read_html(str(table))
    print(df[0].to_json(orient='records'))
