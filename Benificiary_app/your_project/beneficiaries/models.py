from django.db import models

class Beneficiary(models.Model):
    beneficiary_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    contact = models.CharField(max_length=50)
    registration_date = models.DateField()

    def __str__(self):
        return self.name

class ProjectBeneficiaries(models.Model):
    id = models.AutoField(primary_key=True)
    project_id = models.IntegerField()
    beneficiary_id = models.IntegerField()

class BeneficiaryProjectMap(models.Model):
    id = models.AutoField(primary_key=True)
    beneficiary_id = models.IntegerField()
    project_id = models.IntegerField()
    status = models.CharField(max_length=50)
    start_date = models.DateField()

class BeneficiaryDocuments(models.Model):
    id = models.AutoField(primary_key=True)
    beneficiary_id = models.IntegerField()
    document_url = models.URLField()
    doc_type = models.CharField(max_length=100)
