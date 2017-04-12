from django.contrib import admin
from .models import Author, Genre, Book, BookInstance,Language


admin.site.register(Genre)
admin.site.register(Language)


class BookInline(admin.StackedInline):
    model = Book


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


# Register the Admin classes for BookInstance using the decorator

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back', 'book', 'id',)
    list_display = ('book', 'borrower', 'status', 'due_back', 'id')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields':('status', 'due_back', 'borrower',)
        }),
    )


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name','date_of_birth','date_of_death')
        }),
    )
    inlines = [BookInline]



