from rest_framework import routers

from joda_articles import views

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'articles', views.ArticlesViewSet, base_name='articles')
router.register(r'journals', views.JournalsViewSet)
