from django.db import models


class Link(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    original = models.CharField(max_length=255)
    hashed = models.CharField(max_length=20)
    clicks = models.IntegerField(default=0)

    class Meta:
        db_table = 'links'
