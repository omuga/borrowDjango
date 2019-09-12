from rest_framework import serializers
from .models import Borrow

class BorrowSerializer(serializers.ModelSerializer):
    id_prestamista = serializers.IntegerField()
    id_solicitante = serializers.IntegerField()
    fecha_inicio = serializers.DateField()
    fecha_termino = serializers.DateField()
    class Meta:
        model =  Borrow
        fields = ("id","id_prestamista","id_solicitante","fecha_inicio","fecha_termino")
    def create(self, validated_data):
        return Borrow.objects.create(**validated_data)