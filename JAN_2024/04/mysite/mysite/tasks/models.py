from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    done = models.BooleanField(default=False)


def __str__(self):
    return self.title


def __repr__(self):
    return self.title
