from datetime import datetime

from django.contrib import admin

# Register your models here.

from .models import *


class AgentRealEstateInline(admin.TabularInline):
    model = AgentRealEstate
    extra = 0 # Агентите задолжени за одредена недвижност лесно се додаваат во Админ панелот во делот за недвижност


class CharacteristicInline(admin.TabularInline):
    model = RealEstateCharacteristic
    extra = 0  # Карактеристиките за една недвижност исто така се додаваат во делот за недвижности.


class RealEstateAdmin(admin.ModelAdmin):
    inlines = [AgentRealEstateInline, CharacteristicInline]
    list_display = ('name', 'area', 'description',)

    def get_queryset(self, request):
        qs = RealEstate.objects.filter(date_published=datetime.now().date())
        return qs # На супер-корисниците во Админ панелот им се прикажуваат само огласите кои се објавени на денешен датум

    def has_change_permission(self, request, obj = None): # Огласите можат да бидат менувани само од агенти кои се задолжени за продажба на тој оглас, а останатите агенги може само да ги гледаат тие огласи
        return obj and AgentRealEstate.objects.filter(real_estate=obj,agent__user = request.user).exists()

    def has_delete_permission(self, request,
                              obj=None):  # Еден оглас може да биде избришан само ако нема додадено ниту една карактеристика која го опишува
        return not RealEstateCharacteristic.objects.filter(real_estate=obj).exists()

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form,
                           change)  # Огласи за продажба може да бидат додадени само од агенти и по автоматизам агентот кој додава оглас е еден од задолжените за продажба на таа недвижност
        if not change:
            AgentRealEstate.objects.create(real_estate=obj, agent=Agent.objects.filter(user=request.user).first())


class AgentAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'surname',)  # Агентите, Карактеристиките и Недвижностите се прикажани со нивното име (презиме, површина и опис ако ги имаат, соодветно)

    def has_add_permission(self, request):
        return request.user.is_superuser  # Агенти и Карактеристики може да бидат додадени само од супер-корисници


class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def has_add_permission(self, request):
        return request.user.is_superuser  # Агенти и Карактеристики може да бидат додадени само од супер-корисници


admin.site.register(RealEstate, RealEstateAdmin)
admin.site.register(Agent, AgentAdmin)
admin.site.register(Characteristic, CharacteristicAdmin)
admin.site.register(RealEstateCharacteristic)

