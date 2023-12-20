from django.db import models

# Create your models here.
class Movie(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	genre = models.CharField(max_length=30)
	# year = models.DateField()
	year = models.CharField(max_length=4)
	
