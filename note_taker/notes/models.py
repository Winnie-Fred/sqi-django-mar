from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

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
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

