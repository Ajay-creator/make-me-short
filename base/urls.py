from django.urls import path

# views
from . import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('<str:suffix>/',views.Redirect,name='redirect'),
]