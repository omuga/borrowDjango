from django.shortcuts import render
from rest_framework import  viewsets
from .models import Borrow
from .serializers import BorrowSerializer

# Create your views here.
class BorrowView(viewsets.ModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
