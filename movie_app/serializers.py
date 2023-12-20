from rest_framework import serializers
from movie_app.models import Movie

class Movie_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Movie
		fields = '__all__'
		