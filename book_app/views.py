from django.shortcuts import render
from django.http import request,HttpResponse
from django.views.generic.list import ListView
from django.views.generic.base import View
from .models import *
from django.views.generic.edit import CreateView,UpdateView

class index(View):
    def get(self, request):
        return HttpResponse('Welcome')


class BookListView(ListView):
    model = Books
    template_name = 'books/books.html'
    context_object_name = 'books'

class MemberListView(ListView):
    model = Member
    template_name = 'books/members.html'
    context_object_name = 'members'

class BookingListView(ListView):
    model = Booking
    template_name = 'books/booking.html'
    context_object_name = 'bookings'

class Add_booking(CreateView):
    model=Booking
    success_url = '/booking/'
    fields = ['book','member','expiration_date']
    template_name = 'books/add_booking.html'


class updatedate(UpdateView):
    model=Booking
    success_url = '/booking/'
    fields = ['expiration_date']
    template_name = 'books/add_booking.html'
 

       