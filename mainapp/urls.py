from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact',views.contact,name='contact'),
    #path('generate_new_recipe',views.generate_new_recipe,name='generate_new_recipe'),

]