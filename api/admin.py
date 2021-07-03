from  api.models import UsersCrud
from django.contrib import admin

# Register your models here.
 

@admin.register(UsersCrud)
class UserCrudAdmin(admin.ModelAdmin):
    '''Admin View for User'''

    list_display = ('username','email','date_of_birth','profession')
   

