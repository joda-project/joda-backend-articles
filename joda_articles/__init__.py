import os
from joda.version import get_version

default_app_config = 'joda_articles.apps.ArticlesConfig'

version = get_version(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

item_name = 'article'
item_group = 'articles'

print((
    'Joda Articles version %(version)s'
) % {
    'version': version
})
