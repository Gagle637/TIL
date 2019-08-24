from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'update_at', 'created_at',)

admin.site.register(Article, ArticleAdmin)