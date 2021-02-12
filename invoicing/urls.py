from django.urls import path

from . import views

urlpatterns = [
    path('preview', views.preview, name='preview_invoice'),
    path('create', views.create, name='create_invoice'),
]
