from joda_articles.models import Article


def create_from_upload(f):
    article = Article(title=f.name)
    article.save()
    article.files.add(f)
    article.save()
    return article
