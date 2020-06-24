from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index,),
    # path('<int:gid>/search/', views.search,),
    # path('<int:gid>/add/', views.add),
    path('<int:gid>/', views.detail),
]
