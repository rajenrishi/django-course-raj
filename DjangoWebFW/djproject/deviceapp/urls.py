from django.urls import path

from . import views
from .feeds import LastDevicesAdded
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
    path('form_model_device/', views.device_model_form_func_view, name='form_device'),

    # File upload urls
    path('upload_doc/', views.upload_doc, name="upload_doc"),
    path('show_device_doc/', views.show_device_doc, name='show_device_doc'),
    path('customer_details_upload/', views.customer_details_upload, name='customer_details_upload'),

    # Cookies example
    path('set_dev_cookie/', views.set_dev_cookie, name="set_dev_cookie"),
    path('get_dev_cookie/', views.get_dev_cookie, name="get_dev_cookie"),
    path('cookie_demo/', views.cookie_demo, name="cookie_demo"),

    # Test cookie storing capability of browser
    path("test_cookie/", views.test_cookie_session),
    path("test_delete_cookie/", views.test_cookie_delete),


    # Sessions
    path('create_session/', views.create_session, name="create_session"),
    path('get_session/', views.get_session, name="get_session"),
    path('delete_session/', views.delete_session, name="delete_session"),


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



    # Feeds
    path('feeds/', LastDevicesAdded()),

]
