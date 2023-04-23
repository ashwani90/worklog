from .models import Note, Log, Category, Type
from rest_framework import serializers

# to save all this effort we can use HyperLinkedModelSerializer
class NoteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(max_length=1000)
    heading = serializers.CharField(max_length=250)
    def create(self,validated_data):
        return Note.objects.create(**validated_data)
    def update(self,instance,validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.heading = validated_data.get('heading', instance.heading)
        instance.save()
        return instance

    class Meta:
        model = Note
        fields = ['description', 'heading']
        
class LogSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Log
        fields = ['id','description', 'time_spent']
        
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id','description', 'name']
        
class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ['id','description', 'name', 'completed']