from django.shortcuts import render,get_object_or_404
from django.http import Http404
from .models import Book
from django.db.models import Avg


def index(request):
    books = Book.objects.all().order_by('-rating','title')
    num_books = books.count()
    avg_rt = books.aggregate(Avg('rating'))
    return render(request,'book_outlet/index.html',{'books':books,'total_books':num_books,'average_rating':avg_rt})

def book_detail(request,slug):
    '''try:
        book = Book.objects.get(pk=id)
    except:
        raise Http404()'''
    book = get_object_or_404(Book,slug=slug)
    return render(request,'book_outlet/book_detail.html',{
        'title': book.title ,
        'author': book.author,
        'rating': book.rating,
        'is_bestseller': book.is_bestselling
})
