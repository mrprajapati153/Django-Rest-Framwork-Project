from rest_framework import serializers
from .models import CheckList,CheckListItem

class CheckListItemSerializer(serializers.ModelSerializer):
    user=serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model=CheckListItem
        fields=['text','is_checked','created_on','update_on','checklist','user      ']

class CheckListSerializer(serializers.ModelSerializer):
    item=CheckListItemSerializer(source='CheckListItem_set',many=True,read_only=True)
    user=serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model=CheckList
        fields=['title','is_deleted','is_archived','created_on','update_on','item','user']

