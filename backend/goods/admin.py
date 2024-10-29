from django.contrib import admin

from goods.models import Good, Price, Type


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'qty', 'date_update', 'type']
    search_fields = ['title']


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['id', 'value', 'currency', 'good']


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
