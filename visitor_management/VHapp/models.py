from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class hostDetails(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = models.IntegerField()
	address = models.CharField(max_length=100)

class visitor(models.Model):
	name = models.CharField(max_length=30)
	phone = models.IntegerField()
	email = models.EmailField()

class isVisited(models.Model):

	visitor = models.ForeignKey(visitor, on_delete= models.SET_NULL, null=True)
	host = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
	checkin = models.DateTimeField(default=timezone.now)
	checkout = models.DateTimeField(default=timezone.now)
