"""chdeliverybackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf.urls import include,url
from rest_framework.urlpatterns import format_suffix_patterns
from cafe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cafe/', views.UserList.as_view()),
    path('AuthUser/<username>', views.AuthUser.as_view()),
    path('user/', views.CreateUser.as_view()),
    path('foods/', views.Foodlist.as_view()),
    path('order/', views.Order.as_view()),
]

urlpatternsm = format_suffix_patterns(urlpatterns)