from django.contrib import admin
from .models import Goods

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    # This shows the columns in the admin list view
    list_display = ('name', 'price', 'unit', 'is_active', 'user', 'created_at')
    
    # This makes the 'is_active' checkbox clickable directly in the list
    list_editable = ('is_active',)
    
    # This hides the 'user' field in the 'Add Goods' form so it's not manual
    exclude = ('user',)

    # This automatically assigns the logged-in user to the product
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)