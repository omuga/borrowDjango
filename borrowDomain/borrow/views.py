from django.shortcuts import render
from rest_framework import  viewsets
from .models import Borrow
from .serializers import BorrowSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from django.contrib import messages
from django.http import JsonResponse
from django.http import HttpResponse,Http404
from .tasks import verify_del_ids,app   
from celery.result import AsyncResult
from .remote import add



class BorrowView(ListModelMixin, GenericAPIView):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

    def get(self, request, pk = None):
        if pk:
            borrow = get_object_or_404(Borrow.objects.all(),pk = pk)
            serializer = BorrowSerializer(borrow) 
            return Response({"borrow": serializer.data})
        borrows = Borrow.objects.all()
        serializer = BorrowSerializer(borrows,many = True)
        return Response({"borrows": serializer.data})

    def post(self, request):
        borrow = request.data.get('borrow')
        verify_is  = verify_del_ids.delay(int(borrow['id_solicitante']))
        verify_is.get()
        task_out = verify_is.result
        verify_ip = verify_del_ids.delay(int(borrow['id_prestamista']))
        verify_ip.get()
        task_out2 = verify_ip.result
        if (task_out == 200 and task_out2 == 200):
            serializer = BorrowSerializer(data = borrow)
            if serializer.is_valid(raise_exception = True):
                borrow_saved = serializer.save()
            return Response({"success:" "Borrow creates sucessfully"})
        else: 
            return Response({"fail": "Borrow can't be created"})
        
    def update(self,instance, validated_data):
        instance.id_prestamista = validated_data.get('id_prestamista',instance.id_prestamista)
        instance.id_solicitante = validated_data.get('id_solicitante',instance.id_solicitante)
        instance.fecha_inicio = validated_data.get('fecha_inicio',instance.fecha_inicio)
        instance.fecha_termino = validated_data.get('fecha_termino',instance.fecha_termino)
        instance.save()
        return instance
    def put(self, request, pk):
        saved_borrow = get_object_or_404(Borrow.objects.all(), pk=pk)
        data = request.data.get('borrow')
        serializer = BorrowSerializer(instance=saved_borrow, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            borrow_saved = serializer.save()
        return Response({"success": "Borrow '{}' updated successfully".format(borrow_saved.username)})

    def delete(self, request, pk):
        borrow = get_object_or_404(Borrow.objects.all(), pk=pk)
        borrow.delete()
        return Response({"message": "Borrow with id `{}` has been deleted.".format(pk)},status=204)

    def delete_by_field(request,pk):
        try:
            borrow = Borrow.objects.get(id_solicitante = pk)
            serializer = BorrowSerializer(borrow,many = True)
            borrow.delete()
            return HttpResponse(True)   
        except Borrow.DoesNotExist:
            return HttpResponse(False)