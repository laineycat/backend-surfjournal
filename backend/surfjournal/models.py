from django.db import models

# Create your models here.


class SurfJournal(models.Model):
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    surfbreak = models.CharField(max_length=150)
    description = models.TextField()
    notes = models.TextField()
    author = models.CharField(max_length=100)

    def _str_(self):
        return self.country
