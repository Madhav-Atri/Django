from aiohttp import request
from django.shortcuts import render , HttpResponse

def index(request): 
    context = {
        'variable' : "This is sent from views.py"
    }
    return render(request, 'index.html', context)
    
    #return HttpResponse("This is Homepage")
def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')