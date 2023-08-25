from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializers(serializers.ModelSerializer):
    password=serializers.CharField(required=True, write_only=True)
    password2=serializers.CharField(required=True,write_only=True)
    class Meta:
        model=User
        fields=['username','email','password','password2']
        extra_kwargs={
            'password':{'write_only':True},
            'password2':{'write_only':True}
        }
        
    
    def create(self, validated_data):
        username=validated_data.get('username')
        email=validated_data.get('email')
        password=validated_data.get('password')
        password2=validated_data.get('password2')
        
        
        
        
        if password==password2:
            user=User(username=username,email=email)
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError({'error':'password do not match'})
        return super().create(validated_data)