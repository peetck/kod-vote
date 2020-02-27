from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'), # index page
    path('create/', views.create_view, name='create'), # create poll page
    path('vote/<int:poll_id>', views.vote_view, name='vote'),
    path('edit/<int:poll_id>', views.edit_view, name='edit'),
    path('close/<int:poll_id>', views.close_view, name='close'),
    path('delete/<int:poll_id>', views.delete_view, name='delete'),
    path('add_choice/<int:poll_id>', views.add_choice_view, name='add_choice')
]
