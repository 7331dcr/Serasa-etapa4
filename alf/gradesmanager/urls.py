from django.urls import path

from . import views

urlpatterns = [
    path ("", views.index, name="index")

    # API Routes
    path("gabarito", views.gabarito, name="gabarito"),
    path("resposta", views.resposta, name="resposta")
]