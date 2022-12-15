from django.urls import path
from . import views
urlpatterns =[
    path('',views.home),
     path('login',views.login),
     path('update',views.update),
     path('welcome',views.welcome),
      path('base',views.base),
      path('table',views.table)
]