from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('another-page', views.another_page, name='another-page'),
]
