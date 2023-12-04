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
from django.shortcuts import get_list_or_404


#Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user).data,
            "message": "User Created Successfully. Now perform Login to get your token",
        }, status=status.HTTP_201_CREATED)


class DoctorAPI(APIView):

    def get_object(self, pk):
        try:
            return Doctor.objects.get(pk=pk)
        except Doctor.DoesNotExist:
            raise Http404

    def get(self, request,  id=None):
        if id is not None:
            doctor = self.get_object(id)
            serializer = DoctorSerializer(doctor)
            return Response(serializer.data, status=status.HTTP_200_OK)
            # return self.retrieve(request, id)
        
        queryset = Doctor.objects.all()
        serializer = DoctorSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, id):
        obj = self.get_object(id)
        if obj:
            serializer = DoctorSerializer(obj, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response({"error":"Object not found"}, status=status.HTTP_404_NOT_FOUND)

class TreatmentAPI(APIView):

    def get(self, request,  id=None):
        if id is not None:
            obj = get_list_or_404(Doctor, id=id)
            serializer = TreatmentsSerializer(obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
            # return self.retrieve(request, id)
        
        queryset = Doctor.objects.all()
        serializer = TreatmentsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = TreatmentsSerializer(data=request.data)
        # import pdb;pdb.set_trace()
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, id):
        obj = get_list_or_404(Doctor, id=id)
        if obj:
            serializer = TreatmentsSerializer(obj, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response({"error":"Object not found"}, status=status.HTTP_404_NOT_FOUND)


