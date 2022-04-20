"""projekt_main URL Configuration

The `urlpatterns` list routes URLs to views_package. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views_package
    1. Add an import:  from my_app import views_package
    2. Add a URL to urlpatterns:  path('', views_package.home, name='home')
Class-based views_package
    1. Add an import:  from other_app.views_package import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/health/', include('Zadanie2.urls')),
    path('v2/', include('Zadanie2.urls')),
    path('v3/', include('Zadanie2.urls')),
    #path('v2/players/<int:input_player_id>/game_exp', include('Zadanie2.urls')),

]
