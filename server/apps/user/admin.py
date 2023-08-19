from django.contrib import admin
from .models import CustomUser, InvitationCode


@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    pass


@admin.register(InvitationCode)
class InvitationCode(admin.ModelAdmin):
    pass
