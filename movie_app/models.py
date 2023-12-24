from django.db import models

# Inheriting the features of model class
class Movie(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	genre = models.CharField(max_length=30,default=None)
	# year = models.DateField()
	year = models.CharField(max_length=4,default=None)
	
