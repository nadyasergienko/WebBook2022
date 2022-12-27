from django.shortcuts import render, redirect
from django.views import generic
from .models import Book, Author, BookInstance, Genre, Favorites
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(
        status__exact=2).count()
    num_authors = Author.objects.count()
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    return render(request, 'index.html', context={
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits
    })


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Favorites.objects.all()
        filterset = queryset.filter(user=self.request.user).filter(
            favorite__id=self.kwargs['pk'])
        context['is_favorite'] = filterset.count()
        return context


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10


class FavoritesListView(generic.ListView):
    model = Favorites
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        filterset = queryset.filter(user=self.request.user)
        return filterset


def add_favorite(request, book_id):
    if request.method == "POST":
        fav = Favorites(user=request.user,
                        favorite=Book.objects.get(id=book_id))
        fav.save()
        return redirect('book-detail', pk=book_id)


def delete_favorite(request, book_id):
    if request.method == "POST":
        fav = Favorites.objects.get(user=request.user,
                                    favorite=Book.objects.get(id=book_id))
        fav.delete()
        return redirect('book-detail', pk=book_id)


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/book_instance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects \
            .filter(borrower=self.request.user) \
            .filter(status__exact='7') \
            .order_by('due_back')
