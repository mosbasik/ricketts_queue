from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import models

def index(request):
    context = {
        'users': models.User.objects.all(),
    }
    return render(request, 'ricketts_queue/index.html', context=context)

    # return HttpResponse("Hello, world. You're at the Ricketts Queue index.")
