from django.shortcuts import render
from django.shortcuts import redirect

def redirect_to_autorize(request):
    return redirect('/authorize/')
    