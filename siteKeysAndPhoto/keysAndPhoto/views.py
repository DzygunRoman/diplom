from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить файлы", 'url_name': 'add_file'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'},
]

data_db = [
    {'id': 1, 'name': '3 на 4', 'content': ' подходит для большинства документов', 'price': '300р',
     'is_published': True},
    {'id': 2, 'name': '4 на 6', 'content': ' удостоверение охранника, военкомат на контракт', 'price': '300р',
     'is_published': False},
    {'id': 3, 'name': '3,5 на 4,5', 'content': ' паспорт, загран-паспорт', 'price': '300р', 'is_published': True},
]


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'keysAndPhoto/index.html', context=data)


def about(request):
    return render(request, 'keysAndPhoto/about.html', {'title': 'О сайте'})


def show_post(request, post_id):
    return HttpResponse(f"Детальная информация об услуге {post_id}")


def addfile(request):
    return HttpResponse("Добавление файлов")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Войти")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
