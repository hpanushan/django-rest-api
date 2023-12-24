from django.urls import path
from movie_app.views import Movie_List_Create_View, Movie_Update_Delete_View

urlpatterns = [
    # path('<str:model_type>/<str:environment>/<str:table>/', Table_Availability_View.as_view()),
    path('movie', Movie_List_Create_View.as_view()),
    path('movie/<int:id>', Movie_Update_Delete_View.as_view()),
]