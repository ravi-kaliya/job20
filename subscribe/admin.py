from django.contrib import admin
from subscribe.models import Subscribe
# Register your models here.
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'option', )
    list_filter = ('option',)
    search_fields = ('fname', 'lname', 'email', 'option', )
admin.site.register(Subscribe,SubscribeAdmin)