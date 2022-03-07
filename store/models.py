import uuid

from django.db import models
from django.urls import reverse

from category.models import Category

CURRENCY_CHOICES = (
    ("INR", "Indian Rupee"),
    ("USD", "US Dollar"),
    ("EUR", "Euro"),
)


def product_image_upload(instance, filename):
    ext = filename.split(".")[-1]
    name = instance.name.replace(" ", "_")
    # return f"photos/products/{instance.id}_{name}.{ext}"
    return f"photos/products/{name}.{ext}"


class Product(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, blank=True)
    images = models.ImageField(upload_to=product_image_upload, blank=True)
    currency = models.CharField(max_length=50, choices=CURRENCY_CHOICES, default="INR")
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)
    stock = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('product_details', args=(self.category.slug, self.slug))
