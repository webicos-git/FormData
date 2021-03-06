"""FormData URL Configuration

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
from django.contrib.auth.decorators import login_required

from django.contrib import admin
from django.urls import path
from django.conf import settings
from Form import views
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('search/', views.search),
    path('getPdf/', views.getPdf),
    path('createPdf/', views.createPdf),
    path('search/delete/<str:id>/', views.deleteUserData, name="deleteUserData"),
    path('update/<str:id>/', views.update, name="updateUserData"),
    path('downloadReport/', views.downloadReport, name="downloadReport"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
