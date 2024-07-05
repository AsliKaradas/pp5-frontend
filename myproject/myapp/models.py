from django.db import models

# Create your models here.
from django.db import models

class MeinModell(models.Model):
    titel = models.CharField(max_length=200)
    inhalt = models.TextField()
    erstellt_am = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titel