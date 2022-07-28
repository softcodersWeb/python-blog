from django.db import models
from django.utils.text import slugify

# Create your models here.


class Articles(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField(max_length=500)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    slug = models.SlugField(unique=True,max_length=540, blank=True, null=True)
    sub_heading_0 = models.CharField(max_length=500)
    content0 = models.TextField(max_length=500)
    image0 = models.ImageField(null=True, blank=True, upload_to="images/")

    sub_heading_1 = models.CharField(max_length=500)
    content1 = models.TextField(max_length=500)
    image1 = models.ImageField(null=True, blank=True, upload_to="images/")

    sub_heading_2 = models.CharField(max_length=500)
    content2 = models.TextField(max_length=500)
    image2 = models.ImageField(null=True, blank=True, upload_to="images/")

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug= slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
