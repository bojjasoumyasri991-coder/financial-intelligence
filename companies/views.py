from django.shortcuts import render
from rest_framework import generics

from .models import Company
from .serializers import CompanySerializer
from django.shortcuts import get_object_or_404


# -----------------------------
# HOME PAGE
# -----------------------------
from django.http import HttpResponse

def home(request):

    companies = Company.objects.all()

    context = {
        "companies": companies,
        "total_companies": Company.objects.count()
    }

    return render(
        request,
        "home.html",
        context
    )


# -----------------------------
# COMPANY DASHBOARD PAGE
# -----------------------------
def company_dashboard(request, id):

    company = get_object_or_404(
        Company,
        id=id
    )

    return render(
        request,
        "company_dashboard.html",
        {
            "company": company
        }
    )


# -----------------------------
# API - ALL COMPANIES
# -----------------------------
class CompanyListAPIView(generics.ListAPIView):

    queryset = Company.objects.all()
    serializer_class = CompanySerializer


# -----------------------------
# API - SINGLE COMPANY
# -----------------------------
class CompanyDetailAPIView(generics.RetrieveAPIView):

    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    lookup_field = "id"