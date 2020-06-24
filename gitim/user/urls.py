from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>/search/', views.search, name='search'),
    path('<int:id>/add/', views.add, name='add'),
    path('<int:id>/look/', views.look, name='look'),
]
