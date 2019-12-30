from django.db import models
from django.utils import timezone

class user(models.Model):
	name = models.CharField(max_length=20)
	email = models.EmailField()
	phone = models.IntegerField(primary_key=True)
	address = models.CharField(max_length=100)

class host(models.Model):

	phone = models.ForeignKey(user, on_delete= models.SET_NULL)
	password = models.CharField(max_length=16)
	

class isVisited(models.Model):

	visitor = models.ForeignKey(user, on_delete= models.SET_NULL)
	host = models.ForeignKey(host, on_delete= models.SET_NULL)
	checkin = models.DateTimeField(default=timezone.now)
	checkout = models.DateTimeField(default=timezone.now)
