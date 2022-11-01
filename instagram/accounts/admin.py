#
# from django.contrib import admin
# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin
#
# from accounts.models import Account
#
#
# class AccountInline(admin.StackedInline):
#     model = Account
#     fields = ('avatar', 'count_subscriptions', 'count_subscribers', 'description', 'phone', 'gender')
#
#
# class AccountAdmin(UserAdmin):
#     inlines = (AccountInline, )
#
#
# User = get_user_model()
# admin.site.unregister(User)
#
#
# admin.site.register(User, AccountAdmin)
