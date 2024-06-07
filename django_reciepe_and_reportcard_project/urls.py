"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from home.views import *
from vege.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',Home,name='Home'),
    path('update-receipe/<id>/',update_receipe,name='update_receipe'),
    path('delete-receipe/<id>/',delete_receipe,name='delete_receipe'),
    path('receipes/',receipes,name='receipes'),
    path('login/',login_page,name='login_page'),
    path('register/',register,name='register'),
    path('logout/',logout_page,name='logout_page'),
    path('contact/',Contact,name='contact'),
    path('about/',About,name='About'),
    path('success_pg/',success_page,name='successPage'),
    path('students/',get_students,name='get_students'),
    path('admin/', admin.site.urls),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)
    
urlpatterns += staticfiles_urlpatterns()