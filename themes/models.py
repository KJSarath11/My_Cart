from django.db import models

#! Theme Model
class SiteSettings(models.Model):
    banner=models.ImageField(upload_to="site/")
    caption=models.TextField()
