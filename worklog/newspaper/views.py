from django.shortcuts import render
from .models import News, NewspaperContent
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .serializers import NewsSerializer, NewspaperContentSerializer

# Create your views here.
def listing(request):
    data = {
        "news": News.objects.all()
    }
    return render(request,'newspaper/index.html', data)

def newspaper(request):
    data = {
        "news": News.objects.all()
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