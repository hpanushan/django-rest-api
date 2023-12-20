from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

from movie_app.models import Movie
from movie_app.serializers import Movie_Serializer

class Movie_View(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    serializer_class = Movie_Serializer

    def get(self, request):
		
        movie_id = request.query_params.get('movie', None)
        if movie_id:
            movies = Movie.objects.filter(movie_id=movie_id)
        else:
            movies = Movie.objects.all()

        if movies:
            movie_serializer = self.serializer_class(movies, many=True)
            return Response(movie_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message':'No movies found'}, status=status.HTTP_200_OK)
        
    def post(self, request):
		
        name = request.data.get('name', None)
        genre = request.data.get('genre', None)
        year = request.data.get('year', None)
        
        post_data = {
			'name': name,
			'genre': genre,
			'year': year
		}
        
        serializer = self.serializer_class(data=post_data)
        if serializer.is_valid(raise_exception=True):
            movie = serializer.save()
            
        if movie:
            return Response({'message': 'Successful new movie'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        # read data from request
        movie_id = request.query_params.get('movie', None)
        movie = Movie.objects.get(movie_id=movie_id)
        
        if not movie:
            return Response({'message': 'No movies found'})

        else:
            name = request.data.get('name', None)
            if name:
                movie.name = name
                movie.save()

            genre = request.data.get('genre', None)
            if genre:
                movie.genre = genre
                movie.save()

            year = request.data.get('year', None)
            if year:
                movie.year = year
                movie.save()
            return Response({'message': 'Update Complete'}, status=status.HTTP_200_OK)

    def delete(self, request):
        movie_id = request.query_params.get('movie', None)
        movie = Movie.objects.get(movie_id=movie_id)
        
        if not movie:
            return Response({'message': 'No movie found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            movie.delete()
            return Response({'message': 'Movie removed'}, status=status.HTTP_200_OK)

