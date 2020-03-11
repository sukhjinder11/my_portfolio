from django.urls import path
from blog import views

app_name= 'blog'

urlpatterns = [
    path('', views.my_blog, name='my_blog'),
    path('<int:blog_id>/', views.detail, name='detail'),
]
