from django.urls import path,include
from . import views

urlpatterns = [
    path("predict",views.predict,name="predict"),
    path("",views.main,name="main"),
    path("home",views.home,name="home"),
    path("login_user",views.login_user,name="login_user"),
    path("user",views.user,name="user"),
    path("predict",views.predict,name="predict"),
    path("control",views.control,name="control"),
    path("crop",views.crop,name="crop"),
    path("crop1",views.crop1,name="crop1"),
]