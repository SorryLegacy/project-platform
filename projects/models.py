from users.models import Profile

from django.db import models
import uuid


class Tag(models.Model):
    """Model for add tag with hard-skill"""
    name = models.CharField(max_length=100, verbose_name='Tag name')
    slug = models.SlugField(verbose_name='Slug field')
    created = models.DateTimeField(verbose_name='Created date',auto_now_add=True)
    id = models.UUIDField(verbose_name='ID', default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Project(models.Model):
    """Model of project"""
    create_by = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True, verbose_name='User project')
    title = models.CharField(verbose_name='Project title', max_length=100)
    slug = models.SlugField(verbose_name='Slug field')
    description = models.TextField(verbose_name='Project description ', null=True, blank=True)
    tags = models.ManyToManyField(Tag, verbose_name='M2M for tag', blank=True)
    total_votes = models.IntegerField(default=0, null=True, blank=True)
    votes_ratio = models.IntegerField(default=0, null=True, blank=True)
    demo_link = models.CharField(max_length=500, null=True, blank=True)
    source_link = models.CharField(max_length=500, null=True, blank=True)
    created = models.DateTimeField(verbose_name='Created date', auto_now_add=True)
    id = models.UUIDField(verbose_name='ID', default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Review(models.Model):
    """model of comment to project"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Project')
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    review_text = models.TextField(verbose_name='Text for review', null=True, blank=True)
    value = models.CharField(verbose_name='Choice value', max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(verbose_name='Created date', auto_now_add=True)
    id = models.UUIDField(verbose_name='ID', default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value
