from . import views
from django.urls import path
from django.conf.urls import url

app_name = 'auctions'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    url(r'^register/$',views.register, name='register'),
    url(r'^login/$',views.login, name='login'),
]