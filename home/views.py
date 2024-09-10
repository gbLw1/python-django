from django.http import HttpResponse
from django.shortcuts import render

from .models import Usuario

# Create your views here.


def home(request):
    if request.method == "GET":
        return render(request, 'home.html')
    else:
        name = request.POST.get('name')

        if not name:
            return HttpResponse("You need to inform your name!", status=400)

        user = Usuario(nome=name)

        user.save()

        return HttpResponse(f"Hello, {name}!")
