from django.contrib import admin
from .models import ArnUser


class ArnUserAdmin(admin.ModelAdmin):
    model = ArnUser


admin.site.register(ArnUser, ArnUserAdmin)
