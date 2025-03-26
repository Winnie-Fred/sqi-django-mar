from django.db import models


class Category(models.TextChoices):
    WORK = "WK", "Work"
    PERSONAL = "PSNL", "Personal"
    IDEAS = "IDE", "Ideas"

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(choices=Category.choices, max_length=4, default=Category.PERSONAL)
    date_created = models.DateTimeField(auto_now_add=True)

