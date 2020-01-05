from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render

class hostDetails(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = models.IntegerField()
	address = models.CharField(max_length=100)

	def __str__(self):
		return self.user.username

class visitor(models.Model):
	name = models.CharField(max_length=30)
	phone = models.IntegerField(primary_key=True)
	email = models.EmailField()

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('home')

class isVisited(models.Model):

	visitor = models.ForeignKey(visitor, on_delete= models.SET_NULL, null=True)
	host = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
	checkin = models.DateTimeField(default=timezone.now)
	checkout = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f"{self.visitor} - {self.host} : {self.checkin} to {self.checkout}"
