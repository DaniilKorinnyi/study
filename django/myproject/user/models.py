from django.db import models

class User(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField(null=False)


    class Meta:
        db_table = 'user'

    def __str__(self):
        return f"{self.id}: {self.first_name} {self.last_name}"

