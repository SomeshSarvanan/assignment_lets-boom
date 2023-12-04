from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import books
from . serializers import booksSerializer
from rest_framework.decorators import api_view

# @api_view(['GET', 'PUT', 'POST'])
class bookList(APIView):
    
    def get(self, request):
        allBooks = books.objects.all()
        bs = booksSerializer(allBooks, many=True)
        return Response(bs.data)
    
    def post(self, request):
        bs = booksSerializer(data = request.data)
        if(bs.is_valid()):
            bs.save()
            return Response(bs.data, status=status.HTTP_201_CREATED)
    
    def put(self, request, id):
        bs = booksSerializer(book, data = request.data)
        if bs.is_valid():
            bs.save()
            return Response(bs.data)
        return Response(bs.errors, status = status.HTTP_400_BAD_REQUEST)
        

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.

