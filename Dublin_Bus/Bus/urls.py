from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fetch_arrivals/', views.fetch_arrivals, name='arrivaltimes'),
    path('send_to_model', views.send_to_model, name='model'),
    url(r'^twitter$', views.twitter, name='twitter')

]
