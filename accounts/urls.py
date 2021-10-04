from django.urls import path
from .views import HelloView, SignupView, LoginView

urlpatterns = [
    path("hello", HelloView.as_view()),
    path("signup", SignupView.as_view()),
    path("login", LoginView.as_view()),
]
