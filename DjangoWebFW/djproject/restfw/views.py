from django.shortcuts import render
from oauth2_provider.contrib.rest_framework import TokenHasScope
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .serializers import PersonSerializer
from .models import Person


# Create your views here.
# Class based view
class PersonView(APIView):
    def get(self, request):
        return Response({"message": "Person details etc.!"})

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            valid_data = serializer.data

            name = valid_data.get("name")
            age = valid_data.get("age")

            return Response({"message": "Received name {} and age {}.".format(name, age)})
        else:
            return Response({"errors": serializer.errors})


# Function based view
@api_view(['GET', 'POST'])
def person_details(request):
    if request.method == 'GET':
        return Response({"message": "Function based Person details etc.!"})

    if request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            valid_data = serializer.data

            name = valid_data.get("name")
            age = valid_data.get("age")

            return Response({"message": "Received name {} and age {}.".format(name, age)})
        else:
            return Response({"errors": serializer.errors})


@api_view(['GET', 'POST'])
def person_collection(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        # Converting queryset to Python native datatype
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        # Converting request data to python native datatype and
        # validating the data
        if serializer.is_valid():
            # serializer.save()
            # return Response(serializer.data, status=status.HTTP_201_CREATED)

            person_instance = Person.objects.create(**serializer.data)
            return Response({"message": "Created person {}".format(person_instance.id)})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Generic Views
class CreatePerson(ListCreateAPIView):
    # permission_classes = [IsAdminUser]

    # permission_classes = [TokenHasScope]
    # required_scopes = ['write']

    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class ListPerson(ListAPIView):
    # permission_classes = [IsAdminUser]

    # permission_classes = [IsAuthenticated]
    # required_scopes = ['read']
    # authentication_classes = [TokenAuthentication]
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class DeletePerson(DestroyAPIView):
    # permission_classes = [IsAdminUser]
    permission_classes = [IsAuthenticated]

    queryset = Person.objects.all()
    serializer_class = PersonSerializer



from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse

class ApiEndpoint(ProtectedResourceView):
    permission_classes = [TokenHasScope]
    required_scopes = ['read']

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')
