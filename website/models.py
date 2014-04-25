from django.db import models

class project(models.Model):
    name = models.CharField(max_length=200)
    summary = models.CharField(max_length=500)
    description = models.TextField()
    link = models.CharField(max_length=200)

