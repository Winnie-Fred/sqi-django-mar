from django.shortcuts import render, get_object_or_404

from .models import Artist, Album

# Create your views here.
def home(request):
    return render(request, "music/home.html")

def artists(request):
    artists = Artist.objects.order_by("debut_year")
    return render(request, "music/artists.html", {"artists": artists})

def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    return render(request, "music/artist-detail.html", {"artist": artist})

def albums(request):
    albums = Album.objects.order_by("release_date")
    return render(request, "music/albums.html", {"albums": albums})

def album_detail(request, id):
    album = get_object_or_404(Album, id=id)
    return render(request, "music/album-detail.html", {"album": album})