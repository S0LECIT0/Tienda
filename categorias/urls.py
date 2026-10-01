from django.urls import path
from . import views

urlpatterns = {
    path("", views.crear),
    path("lista/", views.listar),
    path("editar/<int:id>/", views.editar),
    path("eliminar/<int:id>/", views.eliminar),
}