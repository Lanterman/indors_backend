from django.urls import path

from . import views

urlpatterns = [
    path("cats/", views.ListCatView.as_view(), name="cat-list"),
    path("cats/<int:id>/", views.CatView.as_view(), name="cat-detail"),
]