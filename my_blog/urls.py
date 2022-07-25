from django.contrib.auth import views as auth
from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('about/', views.about, name='about'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/new/', views.post_new, name='post_new'),
    path('login/', auth.LoginView.as_view(template_name='my_blog/login.html'), name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='my_blog/logout.html'), name='logout')
]
