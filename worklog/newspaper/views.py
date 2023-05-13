from django.shortcuts import render
from .models import News

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

# def view_log(request, log_id):
#     log = get_object_or_404(Log, id=log_id)
#     data = {
#         "log": log
#     }
#     return render(request, "view_log.html", data)