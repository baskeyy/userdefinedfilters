from django.shortcuts import render

# Create your views here.


def filters(request):
    d={'data':'LiFe IS BeaUTifUL SO enjoY EverthINg','matter':'django is best framework in python language'}

    return render(request,'filters.html',d)
