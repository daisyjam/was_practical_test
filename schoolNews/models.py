from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    date = models.DateTimeField(auto_now=False, auto_now_add=False,)
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title
