from django.urls import path
from . import views

urlpatterns = [
    path('', views.alemeno_home_view, name='homepage'),
]
