# Generated by Django 5.0.4 on 2024-04-07 19:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("job", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="adref",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="category",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="company",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="contract_time",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="contract_type",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="country",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="created",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="job_class",
            field=models.CharField(
                blank=True, db_column="__CLASS__", max_length=255, null=True
            ),
        ),
        migrations.AlterField(
            model_name="job",
            name="latitude",
            field=models.DecimalField(
                blank=True, decimal_places=6, max_digits=9, null=True
            ),
        ),
        migrations.AlterField(
            model_name="job",
            name="longitude",
            field=models.DecimalField(
                blank=True, decimal_places=6, max_digits=9, null=True
            ),
        ),
        migrations.AlterField(
            model_name="job",
            name="redirect_url",
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="salary_is_predicted",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="salary_max",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="job",
            name="salary_min",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="job",
            name="title",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
