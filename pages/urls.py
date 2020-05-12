from django.urls import path

from .views import ListView, DetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path("", ListView.as_view(), name="home"),
    path("new/", CreateView.as_view(), name="link_new"),
    path("links/<int:pk>", DetailView.as_view(), name="link_details"),
    path("links/<int:pk>/edit", UpdateView.as_view(), name="link_edit"),
    path("links/<int:pk>/delete", DeleteView.as_view(), name="link_delete"),
]
