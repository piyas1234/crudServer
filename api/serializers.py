from django.db.models import fields
from api.models import UsersCrud
from django.db.models.base import Model
from rest_framework import serializers 



class UserCrudSerializers(serializers.ModelSerializer):
    class Meta:
        model=UsersCrud
        fields = ['id','username','email','date_of_birth','profession','password' ]