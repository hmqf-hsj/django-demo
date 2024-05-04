"""
URL configuration for test_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import testbackend.views as testbackend_views
import page_changer.views as page_changer_views

urlpatterns = [
    path("", page_changer_views.to_test_page),
    path("index", page_changer_views.to_test_page),
    path("test_db", testbackend_views.test_db),
    path("test_post", testbackend_views.test_post),
    path("test_get", testbackend_views.test_get),
]
