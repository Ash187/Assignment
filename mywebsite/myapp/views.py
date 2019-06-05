from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def custom(request):
    dict_var={'template_var' : "It is use to display custom webpage"}
    return render(request, 'myapp/index.html', context=dict_var)
