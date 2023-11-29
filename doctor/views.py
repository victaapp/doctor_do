from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import *
from rest_framework import status
from django.http import Http404
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializer import *
from django.contrib.auth.models import User


#Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })


class DoctorListAPI(APIView):

    def get_object(self, pk):
        try:
            return Doctor.objects.get(pk=pk)
        except Doctor.DoesNotExist:
            raise Http404

    def get(self, request):
        # import pdb;pdb.set_trace()
        # if pk:
        #     snippet = self.get_object(pk)
        #     serializer = DoctorSerializer(snippet)
        #     return Response(serializer.data, status=status.HTTP_200_OK)
        queryset = Doctor.objects.all()
        serializer = DoctorSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrive(self, request, id):
        obj = Doctor.objects.filter(id=id)
        import pdb;pdb.set_trace()
        if obj.exists():
            serializer = DoctorSerializer(obj.first())
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response({"error":"Object not found"}, status=status.HTTP_404_NOT_FOUND)


    def post(self, request, *args, **kwargs):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, id):
        obj = Doctor.objects.filter(id=id)
        if obj.exists():
            serializer = DoctorSerializer(obj.first(), data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response({"error":"Object not found"}, status=status.HTTP_404_NOT_FOUND)
