from django.db import models
from django.db.models import F
from django.urls import reverse
from .season import Season
from django.contrib.auth.models import User

class SchoolClass(models.Model):

    name = models.CharField(max_length=55)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("SClass")
        verbose_name_plural = ("SClasses")

    def __str__(self):
        return f"{self.name}"

    # def get_absolute_url(self):
    #     return reverse("class_detail", kwargs={"pk": self.pk})