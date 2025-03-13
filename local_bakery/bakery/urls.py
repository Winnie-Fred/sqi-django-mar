from django.urls import path

from . import views

app_name = "bakery"

urlpatterns = [
    path("about/", views.about, name="about"),
    path("menu/", views.menu, name="menu"),
    path("contact/", views.contact, name="contact"),
]