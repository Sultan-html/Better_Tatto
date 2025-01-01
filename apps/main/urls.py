from django.urls import path
from apps.main.views import index,blog

urlpatterns = [
    path('', index, name='index'),
    path('blog',blog,name='blog')
]