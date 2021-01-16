from django.forms import model_to_dict
from django.shortcuts import render, redirect
from datetime import datetime
from django.conf import settings

from .models import Project, Comment, Contacts
import re


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    if request.method == "GET":
        return render(request, 'main/contacts.html')
    else:
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        text = request.POST['text']

        pattern_phone = r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$"
        phone_valid = re.match(pattern_phone, phone)
        pattern_email = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
        email_valid = re.match(pattern_email, email)

        if name == '':
            return render(request, 'main/contacts.html', {
                'error': 'Пустое имя'
            })
        if phone == '':
            return render(request, 'main/contacts.html', {
                'error': 'Пустой номер телефона'
            })
        elif not phone_valid:
            return render(request, 'main/contacts.html', {
                'error': 'Неправильный номер телефона'
            })
        if email == '':
            return render(request, 'main/contacts.html', {
                'error': 'Пустой email'
            })
        elif not email_valid:
            return render(request, 'main/contacts.html', {
                'error': 'Неправильный email'
            })
        if text == '':
            return render(request, 'main/contacts.html', {
                'error': 'Пустой текст'
            })
        Contacts(name=name,
                 date=datetime.now(),
                 phone=phone,
                 email=email,
                 text=text).save()
        return render(request, 'main/contacts.html', {
            'error': 'Сообщение успешно отправленно'
        })


def project(request, number_of_project):
    if Project.objects.get(id=number_of_project):
        dictinary = model_to_dict(Project.objects.get(id=number_of_project))
        if request.method == "POST":
            dictinary['comments'] = list(Comment.objects.filter(project=number_of_project))
            author = request.POST['author']
            comment = request.POST['comment']

            if author == '':
                dictinary['error'] = 'Пустое имя'
                return render(request, 'main/project.html', dictinary)
            elif comment == '':
                dictinary['error'] = 'Пустой текст'
                return render(request, 'main/project.html', dictinary)

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
