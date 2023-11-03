from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Ronan: You adjusted this so you could see if the comments were approved in the admin panel...
# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('post', 'author', 'created_on', 'approved',)
    search_fields = ['post', 'author']
    list_filter = ('author', 'approved',  'created_on', )
    actions = ['make_published']

    def make_published(self, request, queryset):
        queryset.update(approved=True)
    make_published.short_description = "Mark selected stories as approved"
    
