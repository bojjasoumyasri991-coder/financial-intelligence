from django.db import models


class Company(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    company_logo = models.TextField(blank=True, null=True)
    company_name = models.CharField(max_length=255)
    chart_link = models.TextField(blank=True, null=True)
    about_company = models.TextField(blank=True, null=True)
    website = models.TextField(blank=True, null=True)
    nse_profile = models.TextField(blank=True, null=True)
    bse_profile = models.TextField(blank=True, null=True)
    face_value = models.FloatField(null=True, blank=True)
    book_value = models.FloatField(null=True, blank=True)
    roce_percentage = models.FloatField(null=True, blank=True)
    roe_percentage = models.FloatField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = "dim_company_full"

    def __str__(self):
        return self.company_name