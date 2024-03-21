"""
URL configuration for project1 project.

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
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.display),

    path('test/car1/', views.card1),
    path('c1', views.card1,name='c1'),
    path('test/car2/', views.card2),
    path('c2', views.card2,name='c2'),
    path('test/car3/', views.card3),
    path('c3', views.card3,name='c3'),

    path('test/car1/pro/', views.card1),
   
    path('test/car2/pro/', views.card2),
    
    path('test/car3/pro/', views.card3),
   

    path('test/lgn/', views.doLogin),
    path('rcv', views.receive,name='rcv'),
    path('rpt1/',views.loginreport),

    path('test/cl/', views.clie),
    path('cli', views.formclient,name='cli'),
    path('rpt3/',views.clientreport),

    path('welcome/', views.show),
    path('get', views.doreviews,name='get'),
    path('rpt5/',views.surveyreport),

    path('test/sgn/', views.getin),
    path('set', views.dosign,name='set'),
    path('rpt2/',views.signreport),
    
    path('test/enq/', views.enqu),
    path('qry', views.doenqui,name='qry'),
    path('rpt4/',views.enquiryreport),
]
