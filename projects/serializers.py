from rest_framework import serializers

from .models import Project, Tag


class TagSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Tag
        fields = ('name',)


class ProjectSerializer(serializers.ModelSerializer):
    """"""
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = ('id', 'title',  'description', 'tags')
