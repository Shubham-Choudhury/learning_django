from django.http import HttpResponse  # import HttpResponse for text response
from django.shortcuts import render  # Render Template

#import datetime for current date
from datetime import datetime


# Render Template
def home(request):
    return render(request, 'index.html')


# Render Text Response
def aboutUS(request):
    return HttpResponse('<center><h1>Welcome to the about us page</h1></center>')

def contactUS(request):
    return HttpResponse('<center><h1>Welcome to the contact us page</h1></center>')


# View for dynamic url
def dynamic(request, my_name):
    # print(type(my_name))
    return HttpResponse(f'<center><h1>Hello \"{my_name}\"</h1></center>')

def dynamic_slug(request, my_slug):
    # print(type(my_slug))
    return HttpResponse(f'<center><h1>Hello \"{my_slug}\"</h1></center>')

def dynamic_int(request, my_int):
    # print(type(my_int))
    return HttpResponse(f'<center><h1>Hello \"{my_int}\"</h1></center>')

def dynamic_auto(request, auto):
    # print(type(my_auto))
    return HttpResponse(f'<center><h1>Hello \"{auto}\"</h1></center>')


# pass data to template
def pass_data(request):
    my_list = [1, 2, 3, 4, 5]
    current_date = datetime.now()
    data = {
        'title': 'Pass Data To Template',
        'my_list': my_list,
        'current_date': current_date,
    }
    return render(request, 'pass_data.html', data)


# Django Template Programming
def django_template_program(request):
    friends = ['Nag', 'Avijit', 'Rahul', 'Sidda']
    data = {
        'friends': friends,
        'age': 17,
        'count': 5,
        'student_details': [
            {'name': 'Nag', 'age': 17, 'marks': 80},
            {'name': 'Avijit', 'age': 17, 'marks': 90},
            {'name': 'Rahul', 'age': 17, 'marks': 70},
            {'name': 'Sidda', 'age': 17, 'marks': 60},
        ],
    }
    return render(request, 'django_template_program.html', data)


# Get Static Files
def get_static_files(request):
    return render(request, 'get_static_files.html')


# Django Template Inheritance
def template_1(request):
    data = {
        'title': 'Template - 1',
    }
    return render(request, 'template_1.html', data)

def template_2(request):
    data = {
        'title': 'Template - 2',
    }
    return render(request, 'template_2.html', data)

def template_3(request):
    data = {
        'title': 'Template - 3',
    }
    return render(request, 'template_3.html', data)

def template_4(request):
    data = {
        'title': 'Template - 4',
    }
    return render(request, 'template_4.html', data)