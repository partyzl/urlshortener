from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class URL(models.Model):
    def __str__(self):
        return self.long

    long = CharField(max_length=200)
