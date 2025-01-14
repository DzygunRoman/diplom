from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string


def index(request):
    t = render_to_string('index.html')
    return HttpResponse(t)


def categories(request, cat_id):
    return HttpResponse("Информация по категориям")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")