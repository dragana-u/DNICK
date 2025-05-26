from django.contrib import admin

from .models import *


# Register your models here.

class AirlinePilotInline(admin.TabularInline):
    model = AirlinePilot
    extra = 0

class AirlineAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [AirlinePilotInline]

class FlightAdmin(admin.ModelAdmin):
    exclude = ('user',)
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(FlightAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj = None):
        if obj and obj.user == request.user:
            return True
        return False

    # def has_delete_permission(self, request, obj = None):
    #     return False

class PilotAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname',)

admin.site.register(Airline, AirlineAdmin)
admin.site.register(Pilot, PilotAdmin)
admin.site.register(Balloon)
admin.site.register(Flight, FlightAdmin)
admin.site.register(AirlinePilot)
