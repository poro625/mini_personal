from django.urls import path
from community import views



urlpatterns = [

    path('', views.ArticleView.as_view(), name='Article_View'),
    path('<int:community_id>/', views.MovieView.as_view(), name='Movie_View'),
    path('<int:community_id>/Movies/', views.MovieView.as_view(), name='Movie_View'),
    path('', views.MovieView.as_view(), name='Movie_View'),
    
]