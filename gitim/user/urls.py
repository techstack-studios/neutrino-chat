from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,),
    path('search/<int:gid>/', views.search,),
    path('add/<int:gid>/', views.add),
    path('detail/<int:gid>/', views.detail),
]
