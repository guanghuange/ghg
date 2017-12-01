from django.contrib import admin

# Register your models here.
from blog.models import Article, Comment, Tag, Category


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = []


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = []


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = []


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = []