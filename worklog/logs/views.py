from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Note, Log, Category, Type
from .serializers import NoteSerializer, LogSerializer, CategorySerializer, TypeSerializer
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test, login_required


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    
class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    
@user_passes_test(lambda user: user.is_staff)
@login_required
def listing(request):
    data = {
        "logs": Log.objects.all()
    }
    return render(request,'listing.html', data)

def view_log(request, log_id):
    log = get_object_or_404(Log, id=log_id)
    data = {
        "log": log
    }
    return render(request, "view_log.html", data)