"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('changecase', views.changecase, name='changecase'),
    path('sorting', views.sorting, name='sorting'),
    path('regex', views.regex, name='regex'),
    path('wordsorting', views.wordsorting, name='wordsorting'),
    path('numbersorting', views.numbersorting, name='numbersorting'),
    path('emailextrator', views.emailextrator, name='emailextrator'),
    path('phonenumextrator', views.phonenumextrator, name='phonenumextrator'),
    path('termsandcondition', views.termsandcondition, name='termsandcondition'),
    path('privacypolicy', views.privacypolicy, name='privacypolicy'),
    path('disclaimer', views.disclaimer, name='disclaimer'),
    path('websitedetail', views.websitedetail, name='websitedetail'),
    path('features', views.features, name='features'),
    path('extraspaceremover', views.extraspaceremover, name='extraspaceremover'),
    path('newlineremover', views.newlineremover, name='newlineremover'),
    path('removepunctuations', views.removepunctuations, name='removepunctuations'),
    path('counter', views.counter, name='counter'),
    path('analyze', views.analyze, name='analyze'),
]
