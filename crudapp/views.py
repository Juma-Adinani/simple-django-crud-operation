from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from crudapp.models import People
from django.urls import reverse
# Create your views here.


def index(request):
    # template = loader.get_template('crudapp/index.html') #=> to be used in a long form
    people = People.objects.all()
    context = {
        'people': people
    }
    # return HttpResponse(template.render(context, request)) #=> a long form
    return render(request, 'crudapp/index.html', context)  # => shortcut


def add(request):
    return render(request, 'crudapp/add.html', {})


def add_record(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    age = request.POST['age']

    person = People(firstname=firstname, lastname=lastname, age=age)
    person.save()
    return HttpResponseRedirect(reverse('index'))


def delete(request, id):
    person = People.objects.get(id=id)
    person.delete()

    return HttpResponseRedirect(reverse('index'))


def update(request, id):
    people = People.objects.get(id=id)
    context = {
        'person': people
    }

    return render(request, 'crudapp/update.html', context)


def update_record(request, id):
    people = People.objects.get(id=id)
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    age = request.POST['age']

    people.firstname = firstname
    people.lastname = lastname
    people.age = age

    people.save()
    return HttpResponseRedirect(reverse('index'))
