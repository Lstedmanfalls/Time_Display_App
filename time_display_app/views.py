from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
    
def index(request):
    context = {
        "date": strftime("%A, %B %d, %Y", gmtime()),
        "time": strftime("%I:%M %p", gmtime()),
    }
    return render(request,'index.html', context)
