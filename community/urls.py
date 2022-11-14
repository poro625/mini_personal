from django.urls import path
from community import views



urlpatterns = [

    path('', views.MovieView.as_view(), name='Movie_View'),
    
]
    
    

