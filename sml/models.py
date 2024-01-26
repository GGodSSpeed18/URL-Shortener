from django.db import models

# Create your models here.
class URLdata(models.Model):
    name = models.TextField(null=False, max_length=25, default=None)
    long_url = models.URLField(null=False)
    short_code = models.TextField(max_length=15, null=True, unique=True)

    def __str__(self):
        return str(self.name)