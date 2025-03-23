from django.urls import path
from . import views

urlpatterns = [
    path('', views.postList, name='blog-home'),
    path('post/<int:pk>/', views.postDetailView, name='post-detail'),
    path('post/new/', views.postCreateView, name='post-create'),
    path('post/<int:pk>/update/', views.postUpdateView, name='post-update'),
    path('post/<int:pk>/delete/', views.postDeleteView, name='post-delete'),
    path('about/', views.about, name='blog-about'),
    #api
    path('api/posts/',views.PostListAPIView.as_view(), name='post-list'),
    path('api/posts/<int:pk>/', views.PostRetriveAPIView.as_view(), name='post-delete'),
    path('api/posts/create',views.PostCreateView.as_view(), name='post-create'),
    path('api/posts/delete/<int:pk>/',views.PostDeleteAPIView.as_view(), name='post-delete'),
    path('api/posts/update/<int:pk>/', views.PostUpdateView.as_view(), name='post-delete'),

]
