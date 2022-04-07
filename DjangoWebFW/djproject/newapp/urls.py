from django.urls import path, re_path, register_converter

from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.DateConverter, 'demodate')

urlpatterns = [
    path('show/', views.show, name='show'),
    # path('movie/<str:name>/', views.movie),
    path('movieyear/<yyyy:year>/', views.movieyear),
    path('showdate/<demodate:dmdate>/', views.showdate),

    re_path('index/(?P<username>\w+)/', views.indexpage),
    re_path('movie/year/(?P<year>[2][0-9]{3})/', views.movieyear),

    path('show_emp_details/<int:empid>/', views.show_emp_details, {'empname': 'Raj'}),

    path('indextemplatedemo/', views.indextemplatedemo),
    path('indexvardemo/', views.indexvardemo),

    path('indexiftagdemo/', views.indexiftagdemo),











    path('indefortagdemo/', views.indefortagdemo),





    path('indeforemptytagdemo/', views.indeforemptytagdemo),
    path('indexcycletagdemo/', views.indexcycletagdemo),
    path('tempindemo/', views.tempindemo),
]
