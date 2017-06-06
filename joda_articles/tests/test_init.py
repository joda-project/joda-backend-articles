from django.test import TestCase

import joda_articles


class InitTestCase(TestCase):

    def test_meta(self):
        """Test meta information"""
        self.assertEqual(joda_articles.model_name, 'Article')
        self.assertEqual(joda_articles.item_name, 'article')
        self.assertEqual(joda_articles.item_group, 'articles')
