from .models import Category


def get_category_list(request):
    category_list = Category.objects.all()
    return dict(category_list=category_list)
