from django.db import models

# Create your models here.


class URL(models.Model):
    link = models.CharField(max_length=200, blank=False)
    uuid = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return str(self.link + "," + self.uuid)
