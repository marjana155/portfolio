from django.contrib import admin
from .models import Blog, Category
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    exclude = ['pub_date']
    list_display = ('title', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
