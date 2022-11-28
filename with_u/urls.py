from django.urls import path
import with_u.views as views

"""
book app urls goes here

"""
urlpatterns = [

    path('',views.index.as_view(),name='home'),
    path('booking/',views.BookingListView.as_view(),name='booking'),
    path('books/',views.BookListView.as_view(),name='books'),
    path('members/',views.MemberListView.as_view(),name='members'),
    path('add_booking/',views.Add_booking.as_view(),name='add_booking'),
    path('upadte_booking/<int:pk>',views.updatedate.as_view(),name='update_booking'),


]