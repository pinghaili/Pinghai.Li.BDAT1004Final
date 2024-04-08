from django.db import models

class Job(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=6, null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True)
    adref = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    contract_type = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    job_class = models.CharField(max_length=255, db_column='__CLASS__', null=True, blank=True)  # Use db_column to handle field names that aren't Python identifiers
    contract_time = models.CharField(max_length=50, null=True, blank=True)
    redirect_url = models.URLField(max_length=1024, null=True, blank=True)
    salary_is_predicted = models.BooleanField(null=True, blank=True)
    description = models.TextField( null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    salary_max = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    salary_min = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

# Create your models here.
