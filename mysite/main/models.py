from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField()
    text = models.TextField()


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    author = models.CharField(max_length=30)
    date = models.DateTimeField()
    comment = models.TextField()


class Contacts(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField()
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    text = models.TextField()