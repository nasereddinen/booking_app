from django.contrib import admin
from .models import *
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'edition')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('member', 'book', 'expiration_date')

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number')


admin.site.register(Books, BookAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Member, MemberAdmin)