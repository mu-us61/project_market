from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view, name="index_view_name"),
    path("items/", views.items_view, name="items_view_name"),
    path("login/", views.login_view, name="login_view_name"),
    path("register/", views.register_view, name="register_view_name"),
    path("logout/", views.logout_view, name="logout_view_name"),
]
