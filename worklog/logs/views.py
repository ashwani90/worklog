from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Note, Log, Category, Type, HealthType, Exercise, HealthLog
from .serializers import NoteSerializer, LogSerializer, CategorySerializer, TypeSerializer, HealthTypeSerializer, ExerciseSerializer, HealthLogSerializer
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
    
class HealthTypeViewSet(viewsets.ModelViewSet):
    queryset = HealthType.objects.all()
    serializer_class = HealthTypeSerializer
    
class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    
class HealthLogViewSet(viewsets.ModelViewSet):
    queryset = HealthLog.objects.all()
    serializer_class = HealthLogSerializer
    
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

def bulk_create_log(request, data):
    pass