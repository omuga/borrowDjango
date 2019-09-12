from django.db import models

# Create your models here.
class Borrow(models.Model):
    id_prestamista = models.IntegerField()
    id_solicitante = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()

    def __init__(self,id_p,id_s,fecha_ini,fecha_ter):
        self.id_prestamista = id_p
        self.id_solicitante = id_s
        self.fecha_inicio = fecha_ini
        self.fecha_termino = fecha_ter
    

