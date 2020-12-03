from django.db import models


# Category model
class Category(models.Model):
    name = models.CharField(max_length=150)
    friendly_name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name