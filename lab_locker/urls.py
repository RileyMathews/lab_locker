from django.urls import path

from .views import index_views
from .views import auth_views

urlpatterns = [
    path("", index_views.index_view, name="index"),
    path("signup", auth_views.signup_view, name="signup"),
    path("signin", auth_views.signin_view, name="signin"),
]
