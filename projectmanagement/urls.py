from django.urls import path

from . import views

urlpatterns = [
    # http://192.168.56.12/projectmanagement/
    path("", views.login, name="login"),
    # http://192.168.56.12/projectmanagement/allusers
    path('allusers', views.allusers, name="allusers"),
    # http://192.168.56.12/projectmanagement/allprojects
    path('allprojects', views.allprojects, name="allprojects"),
    # http://192.168.56.12/projectmanagement/alltasks
    path('alltasks', views.alltasks, name="alltasks"),
    # http://192.168.56.12/projectmanagement/createuser
    path('createuser', views.createuser, name="createuser"),
    # http://192.168.56.12/projectmanagement/createproject
    path('createproject', views.createproject, name="createproject"),
    # http://192.168.56.12/projectmanagement/createtask
    path('createtask', views.createtask, name="createtask"),
    # http://192.168.56.12/projectmanagement/User1
    path('<str:utilisateur>', views.pageutilisateur, name="pageutilisateur")]

