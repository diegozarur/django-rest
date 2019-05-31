from django.test import TestCase
from ..models import Reporter, Article


class ReporterTest(TestCase):

    def setUp(self):
        Reporter.objects.create(
            first_name='Casper', last_name='Alckins', email='casper@mail.com')
        Reporter.objects.create(
            first_name='Jason', last_name='Gradane', email='jason@mail.com')

    def test_reporter(self):
        reporter_casper = Reporter.objects.get(first_name='Casper')
        reporter_jason = Reporter.objects.get(first_name='Jason')
        self.assertEqual(
            reporter_casper.get_reporter(), "Casper Alckins has email: casper@mail.com")
        self.assertEqual(
            reporter_jason.get_reporter(), "Jason Gradane has email: jason@mail.com")


class ArticleTest(TestCase):

    def setUp(self):
        # first_name = 'Jhon', last_name = 'Doe', email = 'teste@mail.com'
        reporter = Reporter(first_name='Jhon', last_name='Doe', email='teste@mail.com')
        reporter.save()

        Article.objects.create(
            headline='Lorem ipsum dolor', pub_date='2019-05-29', reporter_id=reporter.id)
        Article.objects.create(
            headline='Morbi volutpat justo', pub_date='2019-05-29', reporter_id=reporter.id)

    def test_article(self):
        article_lorem = Article.objects.get(headline='Lorem ipsum dolor')
        article_morbi = Article.objects.get(headline='Morbi volutpat justo')
        self.assertEqual(
            article_lorem.get_article(), "Lorem ipsum dolor, 2019-05-29")
        self.assertEqual(
            article_morbi.get_article(), "Morbi volutpat justo, 2019-05-29")
