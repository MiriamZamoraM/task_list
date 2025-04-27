from rest_framework import serializers
from .models import Tasks

class TaskSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Tasks
        exclude = ('status_delete', 'updated')

    
    def create(self, validated_data):
        task = Tasks.objects.create(**validated_data)
        task.save()
        return task
    


class TaskUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('id', 'name', 'description', 'status', 'updated')

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.name = validated_data.get("id", instance.name)
        instance.description = validated_data.get("id", instance.description)
        instance.status = validated_data.get("id", instance.status)
        instance.updated = validated_data.get("id", instance.updated)

        instance.save()
        return instance