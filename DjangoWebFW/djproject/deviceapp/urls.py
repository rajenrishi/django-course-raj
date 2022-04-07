from django.urls import path

from . import views
from .views import DeviceDetailView, DeviceFormView, DeviceListView
from .views import ManufacturerCreateView, ManuUpdateView, ManuDeleteView
from .views import DeviceArchiveIndexView, DeviceYearArchiveView
from .views import DeviceMonthArchiveView, DeviceWeekArchiveView
from .views import DeviceDayArchiveView

from .models import Device

urlpatterns = [
    path('device_actions/', views.device_actions, name='device_actions'),
    path('show_devices_names/', views.show_devices_names, name='show_devices_names'),
    path('show_device_info/<int:id>/', views.show_device_info, name='show_device_info'),
    path('show_first_device/', views.show_first_device, name='show_first_device'),





    path('form_device/', views.device_form_func_view, name='form_device'),










    path('form_manu/', views.manu_form_func_view, name='form_manu'),













    # URLs for class based views
    path('class_based/show_device_list/', DeviceListView.as_view(), name='show_device_list'),
    path('class_based/show_device_details/<int:pk>/', DeviceDetailView.as_view(), name='show_device_details'),
    path('class_based/device_form/', DeviceFormView.as_view(), name='device_form'),
    path('class_based/manu_create/', ManufacturerCreateView.as_view(), name='manu_create'),
    path('class_based/<pk>/manu_update/', ManuUpdateView.as_view(), name='manu_update'),
    path('class_based/<pk>/manu_delete/', ManuDeleteView.as_view(), name='manu_delete'),

    # Date views
    path(
        'class_based/archive/',
        DeviceArchiveIndexView.as_view(model=Device, date_field="device_make_date"),
        name="device_archive"),



    path(
        'class_based/archive/<int:year>/',
        DeviceYearArchiveView.as_view(),
        name="device_year_archive"
    ),
    path(
        'class_based/archive/<int:year>/<int:month>/',
        DeviceMonthArchiveView.as_view(month_format='%m'),
        name="device_month_archive"
    ),
    path(
        'class_based/archive/<int:year>/week/<int:week>/',
        DeviceWeekArchiveView.as_view(),
        name="device_week_archive"
    ),
    path('class_based/archive/<int:year>/<str:month>/<int:day>/',
         DeviceDayArchiveView.as_view(),
         name="device_day_archive"),
]
