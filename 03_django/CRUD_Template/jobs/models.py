from django.urls import reverse
from django.db import models

# Create your models here.
class Jobs(models.Model):
    name = models.CharField(max_length=20)
    past_job = models.TextField()
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("jobs:detail", kwargs={"pk": self.pk})
