from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    
    date_created = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        fields = (
                'id','email','login','firstname','lastname','date_created','password'
            )
        extra_kwargs = {
            'password':{'write_only':True}
        }

