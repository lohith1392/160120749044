from django.urls import path
from .views import NumbersView

urlpatterns = [
    path('numbers', NumbersView.as_view(), name='numbers'),
]
