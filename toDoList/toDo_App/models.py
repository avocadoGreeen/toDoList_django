from django.db import models

class Notes(models.Model):
    title = models.CharField('название', max_length=50)
    description = models.TextField('описание', max_length=1000)
    priority = models.IntegerField()
    date = models.DateTimeField("дата публикации")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def get_absolute_url(self):
        return f'/home/'
