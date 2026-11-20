from django.contrib import admin
from .models import Category,Book,BookCopy
admin.site.register(Category)
class CopyInline(admin.TabularInline):
    model=BookCopy
    extra=1
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=('title','author','isbn','category')
    search_fields=('title','author','isbn')
    inlines=[CopyInline]
admin.site.register(BookCopy)
