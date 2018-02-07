from django.db import models


# Create your models here.
from django.db.models import ForeignKey


class Data(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.key + ' : ' + self.value


class Comment(models.Model):
    data = ForeignKey(Data, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.text