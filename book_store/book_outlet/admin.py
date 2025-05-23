from django.contrib import admin

from .models import Book, Author, Address, Country


class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    # prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'rating',)
    list_display = ('title', 'author', 'rating')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'address')


class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'phone_number', 'city')


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', )


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country, CountryAdmin)
