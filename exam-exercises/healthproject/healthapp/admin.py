from django.contrib import admin

# Register your models here.

from .models import *

class ProductAdmin(admin.ModelAdmin):
    exclude = ('user',)

    def has_change_permission(self, request, obj = None):
        if obj and obj.user == request.user:
            return True
        return False

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(ProductAdmin, self).save_model(request, obj, form, change)


class ProductInline(admin.TabularInline):
    model = Product
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline]
    list_display = ('name',)

    def has_delete_permission(self, request, obj = None):
        if request.user.is_superuser:
            return True
        return False

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')

admin.site.register(Client, ClientAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Sale)