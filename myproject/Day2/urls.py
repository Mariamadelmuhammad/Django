"""Day2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from atexit import register
from django.contrib import admin
from django.urls import path

from affairs.views import home, login, register
from affairs.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('affairs/', home,),
    path('select', selectAll),
    path('login/', login),
    path('logout', mylogout),

    path('register/', register),
    path('delete/<id>', delete),
    path('genericlist', myuserList.as_view(), name='genericlist'),
    path('tracklist', trackList.as_view(), name='tracklist'),
    path('update/<id>', update),





]


# <td class="text-center">
#           <a href="/update/{{user.id}}"
#             ><input class="btn-primary" type="submit" value="Update"
#           /></a>
#         </td>
#         <td class="text-center">
#           <a href="/delete/{{user.id}}"
#             ><input class="btn-primary" type="submit" value="Delete"
#           /></a>
#         </td>
