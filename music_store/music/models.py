from django.db import models

from django.utils import timezone

from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError


def validate_year(year):
    current_year = timezone.now().year
    # if year not in range(1, current_year + 1):
    if not(1 <= year <= current_year):
        raise ValidationError(f"Year must be between 1 and {current_year}.")

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    debut_year = models.IntegerField(validators=[validate_year])
    artist_image = models.ImageField(upload_to="artists/", default="default-artist.jpg")

    def __str__(self):
        return self.name


def validate_release_date(release_date):
    release_year = release_date.year
    current_year = timezone.now().year

    if release_year not in range(1800, current_year + 1):
        raise ValidationError(f"Release year must be between 1800 and {current_year}")



class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")
    title = models.CharField(max_length=255, validators=[MinLengthValidator(2)])
    release_date = models.DateField(validators=[validate_release_date])
    album_cover = models.ImageField(upload_to="album_covers/", blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.artist}"