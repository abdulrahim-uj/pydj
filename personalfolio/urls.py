from django.urls import path
from . import views

app_name = "personalfolio"

urlpatterns = [
    path('', views.base, name='basePage'),
    path('hire/and/contact/', views.contact_me, name='contactMe'),
]
