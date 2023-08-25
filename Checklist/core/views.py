from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CheckListSerializer, CheckListItemSerializer
from .models import CheckList, CheckListItem
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.


class TestAPI(APIView):
    def get(self, request, format=None):
        return Response({'name': 'VINOD  '})


class CheckListsAPIView(APIView):
    # permission_classes=[IsAuthenticated]
    def get(self, request, format=None):
        data = CheckList.objects.all()
        serializer = CheckListSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = CheckListSerializer(data=request.data ,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckListAPIView(APIView):
    serializer_class = CheckListSerializer

    def get_object(self, pk):
        try:
            return CheckList.objects.get(pk=pk)
        except CheckList.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        serializer = self.serializer_class(self.get_object(pk))
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        checklist = self.get_object(pk)
        serializer = self.serializer_class(checklist, data=request.data,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        checklist = self.get_object(pk)
        checklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CheckListItemCreateAPIView(APIView):

    def post(self, request, format=None):
        serializer = CheckListItemSerializer(data=request.data,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def get(self, request,format=None):
    #     data=CheckListItem.objects.all()
    #     serializer=CheckListItemSerializer(data,many=True)
    #     return Response(serializer.data)
    
class CheckListItemAPIView(APIView):
    serializer_class=CheckListItemSerializer
    
    def get_object(self, pk):
        try:
            return CheckListItem.objects.get(pk=pk)
        except CheckList.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        checklist_item=self.get_object(pk)
        serializer = self.serializer_class(checklist_item)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        checklist_item = self.get_object(pk)
        serializer = self.serializer_class(checklist_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        checklist_item = self.get_object(pk)
        checklist_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
      
