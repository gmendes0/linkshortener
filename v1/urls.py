from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.LinkView.as_view()),
    path('<str:shortened>', view=views.LinkView.as_view()),
]
