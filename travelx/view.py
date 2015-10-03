from django.conf import settings
import requests
from django.shortcuts import render
def main(request):
    return render(request,'index.html')
