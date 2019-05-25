from django.shortcuts import render
from django.http import HttpResponse

def print_params(request):
    param_list = [param+'='+str(request.GET.getlist(param)[0]) for param in request.GET.keys()]
    return HttpResponse(str(param_list) + " Hello")
def dynamic(request):
    return render(request, 'base.html')
