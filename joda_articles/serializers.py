from rest_framework_json_api import serializers

from joda_core.documents.serializers import DocumentSerializer
from joda_articles.models import Article, Journal


class ArticleSerializer(DocumentSerializer):

    class Meta(DocumentSerializer.Meta):
        model = Article


class JournalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Journal
        fields = ('id', 'title', 'abbr')
