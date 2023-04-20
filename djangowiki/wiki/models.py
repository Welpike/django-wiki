from django.db import models
from django.utils.text import slugify


class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        print(self.pk)
        super(Article, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = f"{slugify(self.title)}-{self.pk}"
        super().save(*args, **kwargs)
