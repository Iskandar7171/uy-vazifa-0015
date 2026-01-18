from django.urls import path
from .views import CategoryApiView,ProductApiView

urlpatterns = [
    path('category/',CategoryApiView.as_view()),
    path('product/',ProductApiView.as_view())
]