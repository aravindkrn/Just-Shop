from django.db import models
from django.urls import reverse


def category_image_upload(instance, filename):
    ext = filename.split(".")[-1]
    name = instance.name.replace(" ", "_")
    return f"photos/categories/{name}.{ext}"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(upload_to=category_image_upload, blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('products_by_category', args=(self.slug,))
