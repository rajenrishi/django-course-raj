from django.urls import path, include
from rest_framework import routers

from .views import EmployeesList, EmployeeDetail
from .views import EmployeesListGeneric, EmployeeDetailGeneric
from .views import EmployeesViewSet

# For ModelViewSet
router = routers.DefaultRouter()
router.register(r'viewset', EmployeesViewSet)


urlpatterns = [
    ################### APIView ################################
    path('api-view', EmployeesList.as_view()),
    path('api-view/<pk>', EmployeeDetail.as_view()),

    ###################### Concrete Generic views #######################
    path('generic-view', EmployeesListGeneric.as_view()),
    path('generic-view/<pk>', EmployeeDetailGeneric.as_view()),

    ###################### ModelViewSet #######################
    path('', include(router.urls)),
]
