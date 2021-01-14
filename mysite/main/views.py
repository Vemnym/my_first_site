from django.shortcuts import render, redirect
from datetime import datetime


# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


projects = [
    {
        'id': 0,
        'name': 'Имя проекта 1',
        'date': datetime.now(),
        'text': '''Что такое Lorem Ipsum?
                   <br><br>Lorem Ipsum - это текст-"рыба", часто используемый в печати и вэб-дизайне. Lorem Ipsum является стандартной "рыбой" для текстов на латинице с начала XVI века. В то время некий безымянный печатник создал большую коллекцию размеров и форм шрифтов, используя Lorem Ipsum для распечатки образцов. Lorem Ipsum не только успешно пережил без заметных изменений пять веков, но и перешагнул в электронный дизайн. Его популяризации в новое время послужили публикация листов Letraset с образцами Lorem Ipsum в 60-х годах и, в более недавнее время, программы электронной вёрстки типа Aldus PageMaker, в шаблонах которых используется Lorem Ipsum.'''
    },
    {
        'id': 1,
        'name': 'Имя проекта 2',
        'date': datetime.now(),
        'text': '''Почему он используется?
                   <br><br>Давно выяснено, что при оценке дизайна и композиции читаемый текст мешает сосредоточиться. Lorem Ipsum используют потому, что тот обеспечивает более или менее стандартное заполнение шаблона, а также реальное распределение букв и пробелов в абзацах, которое не получается при простой дубликации "Здесь ваш текст.. Здесь ваш текст.. Здесь ваш текст.." Многие программы электронной вёрстки и редакторы HTML используют Lorem Ipsum в качестве текста по умолчанию, так что поиск по ключевым словам "lorem ipsum" сразу показывает, как много веб-страниц всё ещё дожидаются своего настоящего рождения. За прошедшие годы текст Lorem Ipsum получил много версий. Некоторые версии появились по ошибке, некоторые - намеренно (например, юмористические варианты).'''
    },
    {
        'id': 2,
        'name': 'Имя проекта 3',
        'date': datetime.now(),
        'text': '''Почему он используется?
                   <br><br>Давно выяснено, что при оценке дизайна и композиции читаемый текст мешает сосредоточиться. Lorem Ipsum используют потому, что тот обеспечивает более или менее стандартное заполнение шаблона, а также реальное распределение букв и пробелов в абзацах, которое не получается при простой дубликации "Здесь ваш текст.. Здесь ваш текст.. Здесь ваш текст.." Многие программы электронной вёрстки и редакторы HTML используют Lorem Ipsum в качестве текста по умолчанию, так что поиск по ключевым словам "lorem ipsum" сразу показывает, как много веб-страниц всё ещё дожидаются своего настоящего рождения. За прошедшие годы текст Lorem Ipsum получил много версий. Некоторые версии появились по ошибке, некоторые - намеренно (например, юмористические варианты).'''
    }
]


def project(request, number_of_project):
    if number_of_project < len(projects):
        return render(request, 'main/project.html', projects[number_of_project])
    else:
        return redirect('/')


def list_projects(request):
    links = []
    i = 0
    for i in projects:
        text_link = "<a href = '/project/{}'>Проект - {}</a>".format(i['id'], i['name'])
        text_link = dict(link=text_link)
        links.append(text_link)

    return render(request, "main/list_projects.html", {
        'links': links
    })


def create_project(request):
    if request.method == "GET":
        return render(request, 'main/create_project.html')
    else:
        secret = request.POST['secret']
        name = request.POST['name']
        text = request.POST['text']

        projects.append({
            'id': len(projects),
            'name': name,
            'date': datetime.now(),
            'text': text
        })
        return redirect('/list_projects')