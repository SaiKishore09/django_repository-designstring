from django.db import models

class users(models.Model):
    name=models.CharField(max_length=10)
    email=models.IntegerField()

    def __str__(self):
        return self.name
