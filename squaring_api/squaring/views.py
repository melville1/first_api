from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View

class HelloWorldView(View):
    def get(self, request):
        return HttpResponse('Hello world!')

class SquaringView(View):
    def get(self, request,number):
        return HttpResponse(number**2)