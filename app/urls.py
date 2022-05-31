from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('storage', views.storage, name='storage'),
    path('storage_create', views.storage_create, name='storage_create'),
    path('storage_ordered', views.storage_ordered, name='storage_ordered'),
    path('storage_filtrated', views.storage_filtrated, name='storage_filtrated'),
    path('rangesort', views.rangesort, name='rangesort'),
    path('rangesortresult', views.rangesortresult, name='rangesortresult'),

]