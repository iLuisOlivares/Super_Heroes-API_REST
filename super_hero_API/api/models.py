from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()


class Superpower(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Superhero(models.Model):
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    publisher = models.CharField(max_length=15)
    description = models.TextField()
    super_powers = models.ManyToManyField(Superpower)
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, null=True, blank=True)


class SuperVillain(Superhero):
    nemesis = models.CharField(max_length=100)
