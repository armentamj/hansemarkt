from django.shortcuts import render
from goods.models import Goods # Importing the Goods model here to show the goods on the root

def index(request):
    # Only get the items that are marked as 'is_active'
    # Change .order_status to .order_by
    active_goods = Goods.objects.filter(is_active=True).order_by('-created_at')
    active_goods_count = active_goods.count()
    
    # Ensure the context dictionary has key:value pairs for everything
    return render(request, 'homepage/index.html', {
        'goods': active_goods, 
        'count': active_goods_count
    })

def impressum(request):
    return render(request, 'homepage/impressum.html')