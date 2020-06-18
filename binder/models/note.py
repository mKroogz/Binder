from django.db import models
from django.db.models import F
from django.urls import reverse
from .school_class import SchoolClass
from django.contrib.auth.models import User

class Note(models.Model):

    name = models.CharField(max_length=55)
    content = models.CharField(max_length=100000, null=True, blank=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    date =  models.DateField()

    class Meta:
        verbose_name = ("Note")
        verbose_name_plural = ("Notes")

    def __str__(self):
        return f"{self.name}"

    # def get_absolute_url(self):
    #     return reverse("note_detail", kwargs={"pk": self.pk})