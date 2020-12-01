from django.contrib import admin
from .models import Bidder, Vendor
# Register your models here.


@admin.register(Bidder)
class BidderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    search_fields = ('id', 'first_name', 'last_name')
    list_filter = ('id', 'first_name', 'last_name')


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    search_fields = ('id', 'first_name', 'last_name')
    list_filter = ('id', 'first_name', 'last_name')
