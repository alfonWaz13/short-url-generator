from django.db import models

class Link(models.Model):
    original_url = models.URLField(unique=True)
    short_code = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"