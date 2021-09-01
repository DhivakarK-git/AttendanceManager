from django.urls import path,include
from . import views


urlpatterns = [
    path('search?q=link+for+django+admin&oq=link+for+django+index&aqs=chrome..69i57j0i22i30i457.7240j1j4&sourceid=chrome&ie=UTF-8/', views.faclogin, name='faclogin'),
    path('search?q=link+for+django+admin&oq=link+for+django+faculty&aqs=chrome..69i57j0i22i30i457.7240j1j4&sourceid=chrome&ie=UTF-8/', views.updatedindex, name='updatedindex'),
    path('search?q=link+for+django+admin&oq=link+for+django+facultyp&aqs=chrome..69i57j0i22i30i457.7240j1j4&sourceid=chrome&ie=UTF-8/', views.updatedprofile, name='updatedprofile'),
    path('search?q=link+for+django+admin&oq=link+for+django+facultya&aqs=chrome..69i57j0i22i30i457.7240j1j4&sourceid=chrome&ie=UTF-8/', views.updatedadd, name='updatedadd'),
    path('search?q=link+for+django+admin&oq=link+for+django+facultye&aqs=chrome..69i57j0i22i30i457.7240j1j4&sourceid=chrome&ie=UTF-8/', views.editatt, name='editatt'),
    path('search?q=link+for+django+admin&oq=link+for+django+facultyr&aqs=chrome..69i57j0i22i30i457.7240j1j4&sourceid=chrome&ie=UTF-8/', views.fac_report, name='fac_report'),
]
