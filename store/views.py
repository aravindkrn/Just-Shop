from django.http import Http404
from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .serializers import CategorySerializer
from category.models import Category


def store(request, category_slug=None):
    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
    else:
        products = Product.objects.filter(is_available=True)
    product_count = products.count()
    context = {'products': products, 'product_count': product_count}
    return render(request, 'store/store.html', context)


def product_details(request, category_slug, product_slug):
    try:
        product = Product.objects.get(slug=product_slug, category__slug=category_slug)
    except Product.DoesNotExist:
        raise Http404
    context = {'product': product}
    return render(request, 'store/product_detail.html', context)


class CategoryList(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
