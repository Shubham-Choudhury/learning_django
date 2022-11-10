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
    path('admin/', admin.site.urls),
    path('about-us/', views.aboutUS, name='about-us'), # add about-us path
    path('contact-us/', views.contactUS, name='contact-us'), # add contact-us path

    # dynamic url
    path('dynamic/<str:my_name>/', views.dynamic, name='dynamic'), # add dynamic path
    #dynamic url with slug
    path('dynamic-slug/<slug:my_slug>/', views.dynamic_slug, name='dynamic-slug'), # add dynamic-slug path
    #dynamic url with int
    path('dynamic-int/<int:my_int>/', views.dynamic_int, name='dynamic-int'), # add dynamic-int path
    #dynamic url with unknown type
    path('dynamic-auto/<auto>/', views.dynamic_auto, name='dynamic-auto'), # add dynamic-auto path
]
