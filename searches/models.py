from django.db import models
from django.conf import settings

class SearchQuery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    query = models.CharField(max_length=225)
    timestamp = models.DateTimeField(auto_now_add=True)
    