from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('django_project/', views.django_project, name='django_project'),
    path('django_project/details/<int:id>', views.details, name='details'),
]
