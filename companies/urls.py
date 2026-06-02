from django.urls import path
from .views import *

urlpatterns = [

    path('', home, name='home'),

    path(
        'company/<str:id>/',
        company_dashboard,
        name='company_dashboard'
    ),

    path(
        'api/companies/',
        CompanyListAPIView.as_view()
    ),

    path(
        'api/companies/<str:id>/',
        CompanyDetailAPIView.as_view()
    ),

]