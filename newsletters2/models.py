from django.db import models


class Newsletter(models.Model):
    newsletter_email = models.EmailField(max_length=254, null=True, blank=True, unique=True)

    def __str__(self):
        return self.newsletter_email