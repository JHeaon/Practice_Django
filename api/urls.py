from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    # /
    path("", views.BookModelView.as_view(), name="index"),
    # book/
    path("book/", views.BookList.as_view(), name="book_list"),
    # author/
    path("author/", views.AuthorList.as_view(), name="author_list"),
    # publisher/
    path("publisher/", views.PublisherList.as_view(), name="publisher_list"),
    # book/<int:pk>/
    path("book/<int:pk>/", views.BookDetail.as_view(), name="book_detail"),
    # author/<int:pk>/
    path("author/<int:pk>/", views.AuthorDetail.as_view(), name="author_detail"),
    # publisher/<int:pk>/
    path(
        "publisher/<int:pk>/", views.PublisherDetail.as_view(), name="publisher_detail"
    ),
]
