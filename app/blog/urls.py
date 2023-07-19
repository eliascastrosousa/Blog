from django.urls import path
from .views import home,post,about,contact,createpost

urlpatterns = [
    path('', home , name="home"),    
    path('home/', home , name="home"),
    path('createpost', createpost, name="createpost"),
    path('post/<int:id>', post , name="post"),
    path('about', about , name="about"),
    path('contact', contact , name="contact")
]
