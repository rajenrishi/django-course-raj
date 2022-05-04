from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import PersonView, CreatePerson, ListPerson, DeletePerson, ApiEndpoint
from . import views

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/hello', ApiEndpoint.as_view()),
    path('person_details/', PersonView.as_view(), name='person_details'),
    path('func_person_details/', views.person_details, name='func_person_details'),
    path('person_collection/', views.person_collection, name='person_collection'),
    path('cbv/create-person/', CreatePerson.as_view(), name='create_person'),
    path('cbv/list-persons/', ListPerson.as_view(), name='list_person'),
    path('cbv/delete-person/<pk>/', DeletePerson.as_view(), name='delete_person'),
]
