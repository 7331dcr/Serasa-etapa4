from django.urls import path

from . import views

urlpatterns = [
    path ("", views.index, name="index"),

    # API Routes
    path("gabarito", views.cadastrar_gabarito, name="gabarito"),
    path("resposta", views.cadastrar_resposta, name="resposta")
]