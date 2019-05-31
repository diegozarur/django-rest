from rest_framework import viewsets
from core.models import Reporter, Article
from .serializers import ReporterSerializer, ArticleSerializer


class ReporterViewSet(viewsets.ModelViewSet):
    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
