from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    draft = models.BooleanField()

    def __str__(self):
        return self.title
