from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Category,Product
from django.core.paginator import Paginator

@login_required
def dashboard(request):
    context = {
        'total': Product.objects.count(),
        'active': Product.objects.filter(status='active').count(),
        'inactive': Product.objects.filter(status='inactive').count(),
        'low': Product.objects.filter(stock__lte=Product.LOW_STOCK_THRESHOLD).count(),
    }
    return render(request, 'dashboard.html', context)
    
@login_required
def product_list(request):
    products = Product.objects.select_related('category').order_by('-created_at')

    q = request.GET.get('q', '').strip()
    category = request.GET.get('category', '')
    status = request.GET.get('status', '')

    if q:
        products = products.filter(name__icontains=q)
    if category:
        products = products.filter(category_id=category)
    if status:
        products = products.filter(status=status)

    params = request.GET.copy()
    params.pop('page', None)

    page_obj = Paginator(products, 10).get_page(request.GET.get('page'))

    return render(request, 'product_list.html', {
        'page_obj': page_obj,
        'categories': Category.objects.all(),
        'q': q,
        'selected_category': category,
        'selected_status': status,
        'query_string': params.urlencode(),
    })