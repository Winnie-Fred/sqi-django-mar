from django.db import models

from authors.models import Author

# related name
# naive datetime
# automatically calculate total price for orders in ecommerce project

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    number_of_pages = models.PositiveIntegerField()
    published_on = models.DateField()

    def __str__(self):
        return f"{self.title} by {self.author}"