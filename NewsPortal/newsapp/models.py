from django.db import models
from datetime import datetime
from django.urls import reverse

news = 'NW'
article = 'AR'
CATEGORY_CHOISES = [
        (news, 'Новость'),
        (article, 'Статья'),
    ]

class Post(models.Model):
    news = 'NW'
    article = 'AR'
    CATEGORY_CHOISES = [
        (news, 'Новость'),
        (article, 'Статья'),
    ]
    category_type = models.CharField(max_length=2, choices=CATEGORY_CHOISES, default=news)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='posts',
    )

    def __str__(self):
        return f'{self.title.title()[:15]} : {self.description[:30]}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name.title()


