from django.db import models


# Create your models here.
class TvManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title name should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network name should be at least 3 characters"
        if len(postData['description']) < 10 and len(postData['description']) != 0:
            errors["description"] = "Description should be at least 10 characters"
        return errors


class TV_Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.CharField(max_length=255)
    objects = TvManager()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
