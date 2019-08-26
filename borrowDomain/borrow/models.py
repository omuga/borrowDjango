from django.db import models

# Create your models here.
class Borrow(models.Model):
    titulo = models.CharField(max_length= 50)

    def __str__(self):
        return self.titulo
