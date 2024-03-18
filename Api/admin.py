from django.contrib import admin
from .models import Role, User, Ticket

class RoleModelAdmin(admin.ModelAdmin):
    list_display = [
        'title'
    ]

class UserModelAdmin(admin.ModelAdmin):
    list_display = [
        'full_name', 'email'
    ]
    search_fields = ['email', 'full_name']

class TicketModelAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'visiting_time', 'price', 'author'
    ]

admin.site.register(Role, RoleModelAdmin)
admin.site.register(User, UserModelAdmin)
admin.site.register(Ticket, TicketModelAdmin)

