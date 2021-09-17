"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.urls import path, include
from djproject import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', views.home, name='home'),
    path ('cafe/', views.cafe, name='cafe'),
    path ('livingroom/', views.livingroom, name='livingroom'),
    path ('managerroom/', views.managerroom, name='managerroom'),
    path ('restaurant/', views.restaurant, name='restaurants'),
    path ('school/', views.school, name='school'),
    path ('managerroom/', views.managerroom, name='managerroom'),
    path ('sharedoffice/', views.sharedoffice, name='sharedoffice'),
    path ('bedroom/', views.bedroom, name='bedroom'),
    path ('diningroom/', views.diningroom, name='diningroom'),
    path ('falseceiling/', views.falseceiling, name='falseceiling'),
    path ('gym/', views.gym, name='gym'),
    path ('studyroom/', views.studyroom, name='studyroom'),
    path ('kidrroom/', views.kidrroom, name='kidrroom'),
    path ('diningroom/', views.diningroom, name='diningroom'),
    path ('reception', views.reception, name='reception'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('contact', views.contact, name='contact'),
    path('response', views.response, name='response')
]

