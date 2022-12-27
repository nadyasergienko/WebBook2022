from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    re_path(r"^books/$", views.BookListView.as_view(), name="books"),
    re_path(r"^book/(?P<pk>\d+)$",
            views.BookDetailView.as_view(), name="book-detail"),
    re_path(r"^authors/$", views.AuthorListView.as_view(),
            name="authors"),
    re_path(r"^favorites/$", views.FavoritesListView.as_view(),
            name="favorites"),
    re_path(r"^mybooks/$", views.LoanedBooksByUserListView.as_view(),
            name="my-borrowed"),
    path('add_favorite/<int:book_id>/', views.add_favorite, name="add_favorite"),
    path('delete_favorite/<int:book_id>/', views.delete_favorite,
         name="delete_favorite")
]
