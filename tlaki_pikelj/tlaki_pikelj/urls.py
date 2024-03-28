"""
URL configuration for tlaki_pikelj project.

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
from django.urls import path, include
from webpage import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tlaki-pikelj/', views.home_page, name='home_page'),
    path('storitve/', views.services, name='services'),
    path('reference/', views.reference_list, name='references'),
    path('kontakt/', views.contact_info, name='contact'),
    path('narocite-se/', views.order_services, name='order_services'),
    path('potrditev-narocila/', views.order_confirmation, name='order_confirmation'),
]

