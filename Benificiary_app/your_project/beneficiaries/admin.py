from django.contrib import admin
from .models import Beneficiary, ProjectBeneficiaries, BeneficiaryProjectMap, BeneficiaryDocuments

admin.site.register(Beneficiary)
admin.site.register(ProjectBeneficiaries)
admin.site.register(BeneficiaryProjectMap)
admin.site.register(BeneficiaryDocuments)
