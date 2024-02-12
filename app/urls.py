from django.urls import path
from . import views

urlpatterns = [
    path("",views.Home,name="Home"),
    path("result",views.Sum,name="Sum"),
    path("",views.back,name="back")
]
