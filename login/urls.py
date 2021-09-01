from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path("search?q=link+for+django+admin&oq=link+for+django+logout&aqs=chrome..69i57j0i22i30i457.7240j1j4&sourceid=chrome&ie=UTF-8", views.logout_request, name="logout"),
]
