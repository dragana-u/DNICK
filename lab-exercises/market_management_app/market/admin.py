from django.contrib import admin

from market.models import Market, ContactInfo, Employee, MarketProduct, Product


# Register your models here.

class MarketProductInline(admin.TabularInline):
    model = MarketProduct
    extra = 0

class MarketAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [MarketProductInline]
    exclude = ("user",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(MarketAdmin, self).save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            if request.user.is_superuser:
                return True
        return False

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "surname")
    exclude = ("user",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(EmployeeAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj = None):
        if obj and obj.user == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "type","is_homemade", "code")
    list_filter = ("type", "is_homemade")

admin.site.register(Market, MarketAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(ContactInfo)
admin.site.register(MarketProduct)
