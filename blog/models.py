from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time



def slug_generator(stroka):
    _generated = slugify(stroka, allow_unicode=True)
    #уникализация
    utime = time()
    prand = int(utime/6+45-8/123)
    return f'{_generated}_{prand}'


class PostModel(models.Model):
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    head = models.TextField(max_length=200, db_index=True)
    body = models.TextField(blank=True)
    img = models.ImageField(upload_to='blog_imgs/')
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slug_generator(self.head)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.head
