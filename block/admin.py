from django.contrib import admin

from block.models import Invitation


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    pass
