from django.urls import path
from community import views



urlpatterns = [

    path('', views.CommunityView.as_view(), name='community_view'),
    path('<int:community_id>/', views.CommunityDetailView.as_view(), name='comunity_detail_View'),
    path('<int:community_id>/Movies/', views.MovieDetail.as_view(), name='movie_detail_View'),
    path('like/', views.LikeMovies.as_view(), name='likes_View'),
    
]