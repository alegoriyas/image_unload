from django.shortcuts import render, redirect

from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView

from .forms import BookForm
from .models import Book

def index(request):
    return render(request, 'core/index.html')

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'core/upload.html', context)

def book_list(request):
    books = Book.objects.all()
    return render(request, 'core/book_list.html', {
        'books': books
    })

def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/books/')
    else:
        form = BookForm()
    return render(request, 'core/upload_book.html', {
        'form': form
        })

def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('/books/')

class BookListView(ListView):
    
    template_name = 'core/class_book_list.html'
    model = Book
    context_object_name = 'books'
    #paginate_by = 10
    #ordering = ['-created']

class UploadBookView(CreateView):
    model = Book
    #fields = ('title', 'author', 'pdf', 'cover')
    form_class = BookForm
    success_url = reverse_lazy('core:class_book_list')
    template_name = 'core/upload_book.html'