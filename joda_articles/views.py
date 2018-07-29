from django_filters.rest_framework import FilterSet
from rest_framework import filters, viewsets

from joda_core.filters import NumberInFilter
from joda_core.documents.views import DocumentsViewSet
from joda_articles.models import Article, Journal
from joda_articles.serializers import ArticleSerializer, JournalSerializer


class ArticlesFilterSet(FilterSet):
    authors = NumberInFilter(field_name='authors', distinct=True)

    class Meta:
        model = Article
        fields = ('authors', 'journal', 'tags')


class ArticlesViewSet(DocumentsViewSet):
    serializer_class = ArticleSerializer
    filter_class = ArticlesFilterSet

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Article.objects.filter(public=True).order_by('-pk')
        return Article.objects.order_by('-pk')


class JournalsViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all().order_by('title')
    serializer_class = JournalSerializer
