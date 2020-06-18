from django.db import models
from django.db.models import F
from django.urls import reverse
from django.contrib.auth.models import User

class Season(models.Model):

    name = models.CharField(max_length=55)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Season")
        verbose_name_plural = ("Seasons")

    def __str__(self):
        return f"{self.name}"

    # def get_absolute_url(self):
    #     return reverse("season_detail", kwargs={"pk": self.pk})