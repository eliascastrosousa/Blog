from django.urls import path, include
from .views import news
urlpatterns = [
    path('', news, name="news" ),    
    path('news/', news, name="news")
]