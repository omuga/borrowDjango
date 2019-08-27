from rest_framework import serializers
from .models import Borrow

class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Borrow
        fields = ("id","id_prestamista","id_solicitante","fecha_inicio","fecha_termino")