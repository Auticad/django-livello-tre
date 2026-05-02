from django.db import models


class ContactMessage(models.Model):
    contact = models.CharField(max_length=54)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    content = models.TextField()

    def __str__(self):
        return f"{self.contact} - {self.subject}"
