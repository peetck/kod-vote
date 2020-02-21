from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'), # index page
    path('create/', views.create_view, name='create') # create poll page
]
