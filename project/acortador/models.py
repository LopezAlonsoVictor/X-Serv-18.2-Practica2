from django.db import models

# Create your models here.

class Paginas(models.Model):
    url = models.CharField(max_length=128)
    def __str__(self):
        return self.url
