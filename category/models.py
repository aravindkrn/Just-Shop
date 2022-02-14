from django.db import models


def category_image_upload(instance, filename):
    return f"photos/categories/{instance.id}_{filename}"


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
