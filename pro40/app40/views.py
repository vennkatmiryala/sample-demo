from django.shortcuts import render
from app40.models import ProductModel


def ShowIndex(request):
    return render(request,'index.html',{"data":ProductModel.objects.all()})