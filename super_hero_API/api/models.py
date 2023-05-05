from django.db import models

# Create your models here.


class Superhero(models.Model):
    name = models.CharField(max_length=100)
    alter_ego = models.CharField(max_length=100)
    description = models.TextField()
