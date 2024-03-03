from django.shortcuts import render
from django.http import HttpResponse
from containers.models import Container

# Create your views here.

def containers_table(request):
    list_of_containers = Container.objects.all()
    arguments_of_containers = []
    for i in list_of_containers:
        arguments_of_containers.append(list(i.__dict__.values())[2:])
    return render(request, 'containers/containers_table.html', {'containers': arguments_of_containers})