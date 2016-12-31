from django.contrib import admin

from joda_articles.models import Article, Journal


class CommonArticlesAdmin(admin.ModelAdmin):
    ordering = ('title',)


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ['added', 'journal']
    search_fields = ['title', 'authors', 'journal', 'tags', 'doi']
    filter_horizontal = ['authors', 'tags']


admin.site.register(Article, ArticlesAdmin)
admin.site.register(Journal, CommonArticlesAdmin)
