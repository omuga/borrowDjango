from django.db import models

# Create your models here.
class Borrow(models.Model):
    id_prestamista = models.IntegerField()
    id_solicitante = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()


    

