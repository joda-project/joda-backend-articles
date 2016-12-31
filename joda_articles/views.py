from django_filters.rest_framework import FilterSet
from rest_framework import filters, viewsets

from joda_core.filters import NumberInFilter
from joda_articles.models import Article, Journal
from joda_articles.serializers import ArticleSerializer, JournalSerializer


class ArticlesFilterSet(FilterSet):
    authors = NumberInFilter(name='authors', distinct=True)

    class Meta:
        model = Article
        fields = ('authors', 'journal', 'tags')


class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('title')
    serializer_class = ArticleSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter)
    filter_class = ArticlesFilterSet
    search_fields = ('title',)


class JournalsViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all().order_by('title')
    serializer_class = JournalSerializer
