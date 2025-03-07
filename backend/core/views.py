from django.shortcuts import render
import os
from django.conf import settings
from django.http import JsonResponse
from .models import Noticias
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import NoticiaSerializer
# Create your views here.

def home(request):
    return render(request, 'core/template.html')

def historia(request):
    return render(request, 'core/template.html')

def noticias(request):
    noticias_list = Noticias.objects.all().values()  # Use .values() to get a list of dictionaries
    return JsonResponse(list(noticias_list), safe=False)  # Return as JSON

def contacto(request):
    return render(request, 'core/template.html')

def frontend(request):
    return render(request, os.path.join(settings.BASE_DIR, 'frontend', 'build', 'index.html'))

@api_view(['GET'])
def get_noticia(request, id):
    try:
        noticia = Noticias.objects.get(id=id)
        serializer = NoticiaSerializer(noticia)
        return Response(serializer.data)
    except Noticias.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)