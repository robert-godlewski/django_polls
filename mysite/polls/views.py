# views files control the logic of how to output the data
from django.http import HttpResponse
#from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
