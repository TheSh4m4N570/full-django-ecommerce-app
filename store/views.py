from django.shortcuts import render, get_object_or_404
from category.models import Category
from store.models import Product


# Create your views here.
def store(request, slug=None):
    categories = None
    products = None
    if slug is not None:
        categories = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(category=categories, is_available=True)
        products_count = products.count()
    else:
        products_count = Product.objects.count()
        products = Product.objects.all().filter(is_available=True)
    context = {'products_count': products_count, 'products': products}
    return render(request, template_name='store/store.html', context=context)


def product_detail(request, slug=None, product_slug=None):

    try:
        single_product = Product.objects.get(category__slug=slug, slug=product_slug)
    except Exception as e:
        raise e

    context = {'single_product': single_product}
    return render(request, 'store/product_detail.html', context=context)