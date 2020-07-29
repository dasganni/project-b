from django.shortcuts import render

# Create your views here.


def dice(request):
    return render(request, 'dice/dice.html', {})
