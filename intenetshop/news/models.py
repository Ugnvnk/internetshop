from datetime import datetime

from django.db import models


class Articles(models.Model):
    title = models.CharField('Name of article', max_length=50)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    anons = models.CharField('Anons', max_length=50)
    full_text = models.TextField('Article')
    date = models.DateTimeField("Date of publication", default=datetime.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'



