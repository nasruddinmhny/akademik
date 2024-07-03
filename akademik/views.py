
from django.http import HttpResponse

def dashboard(request):
    return HttpResponse('<h1>Selamat datang di project django</h1>')

def kontak(request):
    return HttpResponse('<h1>Ini adalah halaman kontak</h1>')