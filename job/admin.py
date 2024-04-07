from django.contrib import admin
from .models import Job, Company, Category, Location

admin.site.register(Job)
admin.site.register(Company)
admin.site.register(Category)
admin.site.register(Location)

# Register your models here.
