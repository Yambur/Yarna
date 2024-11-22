from django.shortcuts import render


def index(request):
    return render(request, 'products/main.html')

#def index(request):
#    return render(request, 'products/index.html')