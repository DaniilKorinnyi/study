from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.author}: {self.title} {self.price} grn"