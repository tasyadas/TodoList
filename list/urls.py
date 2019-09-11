from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('<int:this_id>/update', views.update),
    path('<int:this_id>/del', views.delete),
]