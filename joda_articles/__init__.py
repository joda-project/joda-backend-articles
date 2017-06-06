import os

VERSION = (0, 1, 0, 'alpha', 1)

default_app_config = 'joda_articles.apps.ArticlesConfig'
module_path = os.path.dirname(os.path.abspath(__file__))

model_name = 'Article'
item_name = 'article'
item_group = 'articles'
new_item_str = 'New Article'
