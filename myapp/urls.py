
from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path('gallery/', views.images, name='gallery'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('collection/', views.collection,name='collection'),
    path('info/', views.info, name='info'),
    path('form/', views.form, name='form'),

]
