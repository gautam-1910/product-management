from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category,Product
from django.core.paginator import Paginator
from .forms import ProductForm
from django.contrib import messages

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

@login_required
def product_form(request, pk=None):
    product = get_object_or_404(Product, pk=pk) if pk else None
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Product saved successfully.')
        return redirect('product_list')
    return render(request, 'product_form.html', {'form': form, 'product': product})

@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})


@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted.')
        return redirect('product_list')
    return render(request, 'product_confirm_delete.html', {'product': product})