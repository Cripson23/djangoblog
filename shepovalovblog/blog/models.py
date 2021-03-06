from django.db import models


class Posts(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Текст поста')
    date = models.DateTimeField('Дата публикации')
    image = models.ImageField('Изображение', upload_to='posts', default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/blog/{self.id}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

