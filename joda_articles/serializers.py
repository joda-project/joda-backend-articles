from rest_framework_json_api import serializers

from joda_core.serializers import ContentSerializer
from joda_articles.models import Article, Journal


class ArticleSerializer(ContentSerializer):

    class Meta(ContentSerializer.Meta):
        model = Article


class JournalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Journal
        fields = ('id', 'title', 'abbr')
