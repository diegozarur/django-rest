from django_filters import models
from rest_framework import serializers
from core.models import Reporter
from core.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    reporter = serializers.CharField(source='reporter.first_name', read_only=True)
    class Meta:
        model = Article
        fields = ('url', 'headline', 'pub_date', 'reporter')


class ReporterSerializer(serializers.HyperlinkedModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Reporter
        fields = ('first_name', 'last_name', 'email', 'articles')
