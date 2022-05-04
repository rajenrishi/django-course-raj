from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import EmployeeSerializer
from .models import Employee


# Create your views here.
############################################################
################### APIView ################################

# GET ALL, GET Instance, POST, UPDATE, DELETE
class EmployeesList(APIView):

    def get(self, request, format=None):
        items = Employee.objects.all()
        serializer = EmployeeSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetail(APIView):

    def get(self, request, pk, format=None):
        item = get_object_or_404(Employee.objects.all(), pk=pk)
        serializer = EmployeeSerializer(item)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        item = get_object_or_404(Employee.objects.all(), pk=pk)
        serializer = EmployeeSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        item = get_object_or_404(Employee.objects.all(), pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


###################### Concrete Generic views #######################
class EmployeesListGeneric(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetailGeneric(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


###################### ModelViewSet #######################
class EmployeesViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

############################################################
