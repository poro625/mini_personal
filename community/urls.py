from django.urls import path
from community import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.CommunityView.as_view(), name='community_view'),
    path('<int:community_id>/', views.CommunityDetailView.as_view(), name='community_detail_view'),
    path('<int:community_id>/comment/', views.CommentView.as_view(), name='coment_view'),
    path('<int:community_id>/comment/<int:comment_id>/', views.CommentDetailView.as_view(), name='comment_detail_view'),
    path('<int:community_id>/like/', views.LikeView.as_view(), name='like_view'),

    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)