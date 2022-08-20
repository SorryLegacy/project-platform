from rest_framework import serializers

from .models import Project, Tag


class TagSerializer(serializers.ModelSerializer):
    """
        Serializer for Tags
        need coz M2M with Project model
    """
    class Meta:
        model = Tag
        fields = ('name',)


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for Projects"""
    tags = TagSerializer(many=True)

    class Meta:
        model = Project
        fields = ('id', 'title',  'description', 'tags', 'create_by')
