from django.db import models


class task(models.Model):
  title=models.CharField(max_length=100,default="")
  is_completed=models.BooleanField(default=False)