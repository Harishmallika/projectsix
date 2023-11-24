"""
URL configuration for projectsix project.

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


from one.views import *

from two.views import *
from three.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book1/',book1,name='book1'),
    path('abd/',abd,name='abd'),
    path('laptop/',laptop,name='laptop'),
    path('dell/',dell,name='dell'),
    path('abd/',abd,name='abd'),
    path('sivakumar/',sivakumar,name='sivakumar'),
]
