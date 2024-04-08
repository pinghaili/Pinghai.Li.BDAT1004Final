# Generated by Django 5.0.4 on 2024-04-07 20:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("job", "0002_alter_job_adref_alter_job_category_alter_job_company_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="latitude",
            field=models.DecimalField(
                blank=True, decimal_places=6, max_digits=12, null=True
            ),
        ),
        migrations.AlterField(
            model_name="job",
            name="longitude",
            field=models.DecimalField(
                blank=True, decimal_places=6, max_digits=12, null=True
            ),
        ),
    ]