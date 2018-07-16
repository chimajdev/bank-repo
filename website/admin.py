from django.contrib import admin

from .models import Contact
# Register your forms here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','timestamp',)
    search_fields  = ('email','timestamp',)
    list_filter  = ('email','timestamp',)

admin.site.register(Contact, ContactAdmin)