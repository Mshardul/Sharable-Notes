from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'login/$', views.Login, name="Login"),
    url(r'register/$', views.Register, name="Register"),
    url(r'my_notes/$', views.MyNotes, name="MyNotes"),
    url(r'shared_notes/$', views.SharedNotes, name="SharedNotes"),
    url(r'logout/$', views.LogOut, name="LogOut"),
    url(r'add_new_note/$', views.AddNewNote, name="AddNewNote"),
    url(r'update_note/$', views.UpdateNote, name="UpdateNote"),
    url(r'delete_note/$', views.DeleteNote, name="DeleteNote"),
    url(r'$', views.Home, name="Home"),
]