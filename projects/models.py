
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")
    long_description = models.TextField()
    website = models.TextField()
    github = models.TextField()
    appstore = models.TextField()
    playstore = models.TextField()