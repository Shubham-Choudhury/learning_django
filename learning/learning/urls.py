"""learning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from learning import views # import views from learning app

urlpatterns = [
    path('', views.home, name='home'),


    path('admin/', admin.site.urls),
    path('about-us/', views.aboutUS, name='about-us'), # add about-us path
    path('contact-us/', views.contactUS, name='contact-us'), # add contact-us path

    # dynamic url
    path('dynamic/<str:my_name>/', views.dynamic, name='dynamic'), 
    #dynamic url with slug
    path('dynamic-slug/<slug:my_slug>/', views.dynamic_slug, name='dynamic-slug'), 
    #dynamic url with int
    path('dynamic-int/<int:my_int>/', views.dynamic_int, name='dynamic-int'), 
    #dynamic url with unknown type
    path('dynamic-auto/<auto>/', views.dynamic_auto, name='dynamic-auto'), 

    # pass data to template
    path('pass-data/', views.pass_data, name='pass-data'), 

    # Django Template Programming
    path('django-template-program/', views.django_template_program, name='django-template-program'), 


    # Get Static Files
    path('get-static-files/', views.get_static_files, name='get-static-files'),


    # Django Template Inheritance
    path('template-1/', views.template_1, name='template-1'),
    path('template-2/', views.template_2, name='template-2'),
    path('template-3/', views.template_3, name='template-3'),
    path('template-4/', views.template_4, name='template-4'),


    # Django Urls
    path('url-1/', views.url_1, name='url-1'),
    path('url-2/', views.url_2, name='url-2'),
    path('url-3/', views.url_3, name='url-3'),
]
