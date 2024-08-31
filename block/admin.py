from django.contrib import admin

from block.models import Invitation, Wish


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    pass


@admin.register(Wish)
class WishAdmin(admin.ModelAdmin):
    pass
