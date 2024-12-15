from django.urls import path

from . import views

# app_name = "books"

urlpatterns = [
    # auth urls
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerUser, name="register"),
    # Books routes
    path("", views.homepage, name="homepage"),  # Default route
    path(
        "book/<int:book_id>/", views.book_detail, name="book_detail"
    ),  # Book detail page
    path("book/add/", views.add_book, name="add_book"),
    path("book/<int:book_id>/edit/", views.edit_book, name="edit_book"),
    path("book/<int:book_id>/delete/", views.delete_book, name="delete_book"),
]
