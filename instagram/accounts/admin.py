
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from accounts.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'avatar', 'count_subscriptions', 'count_subscribers', 'description', 'phone', 'gender')
    list_filter = ('username', 'email', 'gender')
    search_fields = ('username', 'email')
    fields = ('username', 'email', 'avatar', 'count_subscriptions', 'count_subscribers', 'description', 'phone', 'gender')
    readonly_fields = ('id', 'username', 'email')


admin.site.register(Account, AccountAdmin)
