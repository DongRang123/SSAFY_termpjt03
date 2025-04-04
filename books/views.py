from django.shortcuts import render,redirect
from .models import Book
from .forms import BookForm
# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books':books
    }
    return render(request,'books/index.html',context)

def create(request):
    if request.method == "POST":
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

            return redirect('books:index')
    else:
        form = BookForm()
    context = {
        'form':form,
    }
    return render(request, 'books/create.html',context)

def detail(request,pk):
    book = Book.objects.get(pk=pk)

    context ={
        'book':book
    }
    return render(request, 'books/detail.html', context)

def update(request,pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST ,request.FILES, instance= book)
        if form.is_valid():
            form.save()

            return redirect('books:index')
    else:
        form = BookForm(instance= book)
    context = {
        'form':form,
        'book':book,
    }
    return render(request, 'books/update.html',context)


def delete(request,pk):
    book = Book.objects.get(pk=pk)
    book.delete()

    return redirect('books:index')