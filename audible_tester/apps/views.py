from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def dashboard(req):

    # TODO: pull this data from the database
    data = {
        "user": {
            "username": "mhynson",
            "password": "abc1234",
            "is_authenticated": False,
            "library": [
                {
                    "title": "Money Master the Game",
                    "author": "Tony Robbins",
                },
                {
                    "title": "Becoming",
                    "author": "Michelle Obama"
                }
            ]
        }
    }

    template = loader.get_template('views/dashboard.html')
    rendered_template = template.render(data, req)
    return HttpResponse(rendered_template)


def login(req):
    return render(req, 'views/login.html')


def logout(req):
    return render(req, 'views/logout.html')


def register(req):
    return render(req, 'views/register.html')


def book_add(req):
    return render(req, 'views/book_add.html')


def book_remove(req):
    return render(req, 'views/book_remove.html')
