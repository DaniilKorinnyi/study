from django.contrib import admin

from purchase.models import Purchase


@admin.register(Purchase)
class Purchase(admin.ModelAdmin):
    pass

