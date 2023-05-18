from .models import NewspaperContent, News
from rest_framework import serializers

     
class NewspaperContentSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = NewspaperContent
        fields = ['id','page_num', 'vlocation', 'hlocation', 'heading', 'description', 'date', 'by', 'from_ref']
        
class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ['id','new_head', 'description', 'source', 'type', 'approved']