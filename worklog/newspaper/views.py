from django.shortcuts import render
from .models import News, NewspaperContent
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .serializers import NewsSerializer, NewspaperContentSerializer
from datetime import date



# Create your views here.
def listing(request):
    data = {
        "news": News.objects.all()
    }
    return render(request,'newspaper/index.html', data)

def newspaper(request,id=0):
    if not id:
        id = 0
    today = date.today()
    d2 = today.strftime("%A, %B %d, %Y")
    d1 = today.strftime("%Y-%m-%d 00:00:00")
    data = News.objects.filter(type=id, created_at__gte=d1)
    updatedData = []
    i = 0
    for da in data:
        if i == 20:
            break
        newsItem = {}
        newsItem['head'] = da
        if len(da.description) < 200:
            continue
        desc = da.description.split('.')[:30]
        desc = '.'.join(desc)
        newsItem['description'] = desc
        updatedData.append(newsItem)
        i = i+1
    data = {
        "news": updatedData, "today": d2
    }
    return render(request,'newspaper/edit_news_view..html', data)

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = LargeResultsSetPagination
    
class NewspaperContentViewSet(viewsets.ModelViewSet):
    queryset = NewspaperContent.objects.all()
    serializer_class = NewspaperContentSerializer
    pagination_class = LargeResultsSetPagination

# def view_log(request, log_id):
#     log = get_object_or_404(Log, id=log_id)
#     data = {
#         "log": log
#     }
#     return render(request, "view_log.html", data)