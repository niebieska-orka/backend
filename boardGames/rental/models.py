from django.db import models
from django.utils import timezone


class Person(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    mail = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Game(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Reservation(models.Model):
    borrower = models.ForeignKey(Person, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField(default=timezone.now)
    borrow_date = models.DateTimeField()
    taken_to_home = models.BooleanField(default=True)
    game_returned = models.BooleanField(default=False)
