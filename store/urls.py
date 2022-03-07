from django.urls import path

from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('api/category-list/', views.CategoryList.as_view(), name="category_list"),
    path('<slug:category_slug>/', views.store, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_details, name="product_details"),
]
