from django.contrib import admin

from joda_core.documents.admin import DocumentsAdmin
from joda_articles.models import Article, Journal


class CommonArticlesAdmin(admin.ModelAdmin):
    ordering = ('title',)


class ArticlesAdmin(DocumentsAdmin):
    list_filter = ['created_at', 'changed_at', 'journal']
    search_fields = ['title', 'authors', 'journal', 'tags', 'doi']
    filter_horizontal = ['authors', 'sections', 'tags']


admin.site.register(Article, ArticlesAdmin)
admin.site.register(Journal, CommonArticlesAdmin)
