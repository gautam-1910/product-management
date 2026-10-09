from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Product

@login_required
def dashboard(request):
    context = {
        'total': Product.objects.count(),
        'active': Product.objects.filter(status='active').count(),
        'inactive': Product.objects.filter(status='inactive').count(),
        'low': Product.objects.filter(stock__lte=Product.LOW_STOCK_THRESHOLD).count(),
    }
    return render(request, 'dashboard.html', context)