from django.db import models

# Create your models here.


class Instagram(models.Model):
    long_access_token = models.CharField(max_length=255, null=True, blank=True)
    token_type = models.CharField(max_length=255, null=True, blank=True)
    expires_in = models.CharField(max_length=255, null=True, blank=True)
    user_id = models.CharField(max_length=255, null=True, blank=True)

    instagram_id = models.CharField(max_length=255, null=True, blank=True)
    instagram_username = models.CharField(max_length=255, null=True, blank=True)

    expired = models.DateTimeField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "expired %s" % self.expired