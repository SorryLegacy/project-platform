from django.contrib.auth import get_user_model
from django.db import models
import uuid

User = get_user_model()


class Skill(models.Model):
    """Model about hard_skill that the user have """
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Skills name')
    slug = models.SlugField(verbose_name='Slug')
    description = models.TextField(null=True, blank=True, verbose_name='Description')
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False, verbose_name='ID')

    def __str__(self):
        return self.name


class Profile(models.Model):
    """Model to see some info about user"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User', null=True, blank=True)
    username = models.CharField(max_length=50, verbose_name='Username')
    name = models.CharField(max_length=30, verbose_name='Name', null=True, blank=True)
    email = models.EmailField(max_length=100, verbose_name='User email', null=True, blank=True)
    city = models.CharField(max_length=50, verbose_name='City')
    bio = models.TextField(blank=True, null=True, verbose_name='Bio')
    hard_skill = models.ManyToManyField(Skill, blank=True, verbose_name='Skills',related_name='hard_skill')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False, verbose_name='ID')

    def __str__(self):
        return self.username
