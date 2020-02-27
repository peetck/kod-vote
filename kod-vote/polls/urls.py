from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'), # index page

    path('create/', views.create_view, name='create'), # create poll page

    path('detail/<int:poll_id>', views.detail_view, name='detail'), # detail poll page

    path('vote/<int:choice_id>', views.vote_view, name='vote'), # user vote to poll

    path('edit/<int:poll_id>', views.edit_view, name='edit'), # edit poll page

    path('close/<int:poll_id>', views.close_view, name='close'), # close poll (end poll)

    path('poll_delete/<int:poll_id>', views.poll_delete_view, name='poll_delete'), # delete poll

    path('add_choice/<int:poll_id>', views.add_choice_view, name='add_choice'), # add choice to some poll

    path('choice_delete/<int:choice_id>', views.choice_delete_view, name='choice_delete') # delete choice
]
