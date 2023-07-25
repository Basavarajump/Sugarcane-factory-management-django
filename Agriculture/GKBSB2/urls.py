"""GKBSB2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from MCA.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('reg',reg),
    path('reg1',reg1),
    path('index',index),
    path('login11',login11),
    path('logout',logout),
    path('issue',issue),
    path('userindex<int:proid>',userindex,name="userindex"),
    path('useD',useD),
    path('pdf',pdf),
    path('sav',sav),
    path('pd',pd),
    path('login1',login1),
    path('admin11',admin11),
    path('profile',profile),
    path('preview<int:show>',preview,name="preview"),
    path('pre<int:show1>',pre,name="pre"),
    path('mail',mail),
    
    path('profile1<int:issueid>',profile1,name="profile1"),

  

    ]