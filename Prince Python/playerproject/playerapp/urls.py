from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('add_player/',views.add_player,name='add_player'),
    path('edit/<int:id>/',views.edit_player,name='edit_player'),
]