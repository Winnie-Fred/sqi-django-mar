from django.urls import path

from . import views

app_name = "music"

urlpatterns = [
    path('', views.home, name="home"),
    path('artists/', views.artists, name="artists"),
    path('albums/', views.albums, name="albums"),
    path('artist/<int:artist_id>/', views.artist_detail, name="artist_detail"),
    path('album/<int:id>/', views.album_detail, name="album_detail"),
]