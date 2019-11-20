from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    url(r'^diagnosis', views.diagnosis, name='diagnosis-page'),
    url(r'^register/', views.register, name='register-page'),
    url(r'^login/', views.login, name='login-page'),
    url(r'^', views.home, name='home-page'),

    
]
