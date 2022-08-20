from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from .models import Profile, Skill


class SkillSerializer(PrimaryKeyRelatedField, serializers.ModelSerializer):
    """
        Serializer for SKills
        need coz M2M with Profile model
    """
    class Meta:
        model = Skill
        fields = ('name', )


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for Profiles"""
    hard_skill = SkillSerializer(many=True, queryset=Skill.objects.all())

    class Meta:
        model = Profile
        fields = ('username', 'email', 'bio', 'hard_skill', 'city')
