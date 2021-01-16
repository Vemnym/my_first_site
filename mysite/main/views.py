from django.forms import model_to_dict
from django.shortcuts import render, redirect
from datetime import datetime
from django.conf import settings

from .models import Project, Comment


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def project(request, number_of_project):
    if number_of_project < len(Project.objects.all()) + 1:
        dictinary = model_to_dict(Project.objects.get(id=number_of_project))
        if request.method == "POST":
            author = request.POST['author']
            comment = request.POST['comment']

            if author == '':
                dictinary['error'] = 'Пустое имя'
            elif comment == '':
                dictinary['error'] = 'Пустой текст'

            Comment(project=Project.objects.get(id=number_of_project),
                    author=author,
                    date=datetime.now(),
                    comment=comment.replace("\n", "<br>")).save()

        dictinary['comments'] = list(Comment.objects.filter(project=number_of_project))

        return render(request, 'main/project.html', dictinary)
    else:
        return redirect('/')


def list_projects(request):
    links = []
    for i in Project.objects.all():
        text_link = "<a href = '/project/{}'>Проект - {}</a>".format(i.id, i.name)
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

        if secret != settings.SECRET_KEY:
            return render(request, 'main/create_project.html', {
                'error': 'Неправильный secret key'
            })
        if name == '':
            return render(request, 'main/create_project.html', {
                'error': 'Пустое имя'
            })
        if text == '':
            return render(request, 'main/create_project.html', {
                'error': 'Пустой текст'
            })

        Project(name=name, date=datetime.now(), text=text.replace("\n", "<br>")).save()
        return redirect('/list_projects')
