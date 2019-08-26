from django.urls import path
from indexapp import views

app_name='indexapp'
urlpatterns = [
    path('index/',views.index,name='index'),
    path('booklist/',views.booklist,name='booklist'),
    path('Bookdetails/',views.Bookdetails,name='Bookdetails'),
]