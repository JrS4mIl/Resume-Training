from django.contrib import admin

# Register your models here.
from .models import Message
#
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','message','created_date','update_date']
    search_fields = ['name','subject']




    class Meta:
        model=Message