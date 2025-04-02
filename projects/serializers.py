from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'technology', 'completed', 'create_at', 'updated_at']
        read_only_fields = ['create_at', 'updated_at']

    def create(self, validated_data):
        validated_data['password'] = validated_data.get('password', '')
        return Project.objects.create(**validated_data)    