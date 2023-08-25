from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CheckList(models.Model):
    title=models.CharField(max_length=100)
    is_deleted=models.BooleanField(default=False)
    is_archived=models.BooleanField(default=False)
    created_on=models.DateTimeField(auto_now_add=True)
    update_on=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class CheckListItem(models.Model):
    text=models.CharField(max_length=100)
    is_checked=models.BooleanField(default=True)
    created_on=models.DateTimeField(auto_now_add=True)
    update_on=models.DateTimeField(auto_now=True)
    checklist=models.ForeignKey(CheckList,on_delete=models.CASCADE,related_name='CheckListItem_set')
    user=models.ForeignKey(User,on_delete=models.CASCADE)