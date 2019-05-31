from rest_framework import serializers
from core.models import Reporter
from core.models import Article


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        # fields = '__all__'
        fields = ('headline', 'pub_date')


class ReporterSerializer(serializers.HyperlinkedModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Reporter
        fields = ('first_name', 'last_name', 'email', 'articles')
