from django.db import models

class Company(models.Model):
    display_name = models.CharField(max_length=255)
    class_name = models.CharField(max_length=255)

    def __str__(self):
        return self.display_name

class Location(models.Model):
    area = models.JSONField()  # Stores the area as a list
    display_name = models.CharField(max_length=255)
    class_name = models.CharField(max_length=255)

    def __str__(self):
        return self.display_name

class Category(models.Model):
    tag = models.CharField(max_length=100)
    label = models.CharField(max_length=255)
    class_name = models.CharField(max_length=255)

    def __str__(self):
        return self.label
    
class Job(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    adref = models.CharField(max_length=255)
    created = models.DateTimeField()
    contract_type = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    job_class = models.CharField(max_length=255, db_column='__CLASS__')  # Use db_column to handle field names that aren't Python identifiers
    contract_time = models.CharField(max_length=50)
    redirect_url = models.URLField(max_length=1024)
    salary_is_predicted = models.BooleanField()
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2)
    salary_min = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Create your models here.
