from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("todos/", views.todos, name="Todos"),
]