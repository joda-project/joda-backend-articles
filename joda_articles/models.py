from django.db import models

from joda_core.models import Author
from joda_core.documents.models import Document


class Journal(models.Model):
    title = models.CharField(max_length=255, unique=True, db_index=True)
    abbr = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title

    class JSONAPIMeta:
        resource_name = 'journals'


class Article(Document):
    authors = models.ManyToManyField(Author, blank=True)

    journal = models.ForeignKey(Journal, blank=True, null=True)
    pages = models.CharField(max_length=32, blank=True)
    volume = models.PositiveIntegerField(blank=True, null=True)
    issue = models.PositiveIntegerField(blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True)

    doi = models.CharField(max_length=255, blank=True)
    arxiv = models.CharField(max_length=255, blank=True)
    cds = models.CharField(max_length=255, blank=True)

    class JSONAPIMeta:
        resource_name = 'articles'
