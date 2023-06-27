from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()


# class Superpower(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()


class Character(models.Model):
    superhero_name = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    publisher = models.CharField(max_length=15)
    description = models.TextField()
    # super_powers = models.ManyToManyField(Superpower)
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, null=True, blank=True)
    first_appearance = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    race = models.CharField(max_length=100)
    image = models.CharField(max_length=150)


class Superhero(Character):
    pass


class Supervillain(Character):
    nemesis = models.CharField(max_length=100)
