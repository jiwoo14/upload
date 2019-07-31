from django.db import models

# Create your models here.

class Hello(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=200)
    img = models.ImageField(blank=True, null=True)
