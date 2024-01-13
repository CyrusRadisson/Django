from django.urls import path

from . import views

urlpatterns= [
    path("", views.index, name= "index"),
    path("<str:name>", views.greet, name="greet"),
    path("cyrus", views.Cyrus, name= "Cyrus"),
    path("radisson", views.Radisson, name= "radisson")
]