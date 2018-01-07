from django.db import models
from django.utils.translation import ugettext_lazy as _

from joda_core.models import Author
from joda_core.documents.models import Document


class Journal(models.Model):
    title = models.CharField(max_length=255, unique=True,
                             db_index=True, verbose_name=_('title'))
    abbr = models.CharField(max_length=255, blank=True,
                            verbose_name=_('abbreviation'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('journal')
        verbose_name_plural = _('journals')

    class JSONAPIMeta:
        resource_name = 'journals'


class Article(Document):
    authors = models.ManyToManyField(
        Author, blank=True, verbose_name=_('authors'))

    journal = models.ForeignKey(
        Journal, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=_('journal'))
    pages = models.CharField(max_length=32, blank=True,
                             verbose_name=_('pages'))
    volume = models.PositiveIntegerField(
        blank=True, null=True, verbose_name=_('volume'))
    issue = models.PositiveIntegerField(
        blank=True, null=True, verbose_name=_('issue'))
    year = models.PositiveIntegerField(
        blank=True, null=True, verbose_name=_('year'))

    doi = models.CharField(max_length=255, blank=True,
                           verbose_name=_('DOI'))
    arxiv = models.CharField(max_length=255, blank=True,
                             verbose_name=_('arXiv'))
    cds = models.CharField(max_length=255, blank=True,
                           verbose_name=_('CDS'))

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')

    class JSONAPIMeta:
        resource_name = 'articles'
