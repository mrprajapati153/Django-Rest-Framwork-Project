
from django.urls import path
from . import views

urlpatterns = [
    
    path('api/checklist/',views.CheckListsAPIView.as_view(),name='CheckLists'),
    path('api/checklist/<int:pk>/',views.CheckListAPIView.as_view(),name='CheckList'), 
    path('api/checklist/create/',views.CheckListItemCreateAPIView.as_view(),name='CheckListitems'),
    path('api/checklists/<int:pk>/',views.CheckListItemAPIView.as_view(),name='CheckListitem')
    
]
