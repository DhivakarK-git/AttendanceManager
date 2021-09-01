from django.urls import path,include
from . import views


urlpatterns = [
    path('search?q=link+for+django+admin&oq=link+for+django+index&aqs=chrome..69i57j0i22i30i457.7240j1j4&sourceid=chrome&ie=UTF-8/', views.studlogin, name='studlogin'),
    path('search?q=link+for+django+admin&oq=link+for+django+faculty&aqs=chrome..69i57j0i22i30i457.7240j1j4&sourceid=chrome&ie=UTF-8/', views.studindex, name='studindex'),
    path('search?q=link+for+django+admin&oq=link+for+django+facultyp&aqs=chrome..69i57j0i22i30i457.7240j1j4&sourceid=chrome&ie=UTF-8/', views.studprofile, name='studprofile'),
    path('search?q=link+for+django+admin&oq=link+for+django+facultya&aqs=chrome..69i57j0i22i30i457.7240j1j4&sourceid=chrome&ie=UTF-8/', views.studadd, name='studadd'),
    path('search?q=link+for+django+admin&oq=link+for+django+facultyr&aqs=chrome..69i57j0i22i30i457.7240j1j4&sourceid=chrome&ie=UTF-8/', views.stud_report, name='stud_report'),
]
