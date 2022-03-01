from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

#customise admin UI of accounts table
 #it will display rows of table data

class AccountAdmin(UserAdmin):
    list_display = ( 'first_name', 'last_name', 'user_name', 'email', 'last_login', 'date_joined', 'is_superadmin')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('-date_joined',)

# Register your models here.
admin.site.register(Account, AccountAdmin)