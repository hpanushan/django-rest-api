from django.urls import path
from movie_app.views import Movie_View

urlpatterns = [
    # path('<str:model_type>/<str:environment>/<str:table>/', Table_Availability_View.as_view()),
    path('', Movie_View.as_view()),
]