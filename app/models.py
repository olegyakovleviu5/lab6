from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.


class User_1(models.Model):
    UserId = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20,null=True)
    last_name = models.CharField(max_length=20,null=True)
    phone = models.PositiveIntegerField( unique=True)
    email = models.EmailField(max_length=50, unique=True)
    birthday = models.DateField(blank=True)
    passport = models.PositiveIntegerField(unique=True,null=True)


class Team(models.Model):
    TeamId = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=30,unique=True,null=True)
    rating = models.PositiveSmallIntegerField(null=True)
    sport = models.CharField(max_length=30,null=True)
    number_of_players = models.PositiveSmallIntegerField(null=True)


class Bet(models.Model):
    BetId = models.AutoField(primary_key=True)
    user = models.ForeignKey(User_1, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.FloatField(null=True)


