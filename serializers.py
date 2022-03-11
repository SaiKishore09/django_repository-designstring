from rest_framework import serializers
from . models import users

class userserializers(serializers.ModelSerializer):

    class Meta:
        model=users
        fields=('name','email')
        fields='__all__'

