# Generated by Django 4.0.1 on 2022-02-25 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0031_project_apilink'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('From_Where', models.CharField(blank=True, max_length=200, null=True)),
                ('Year_of_qualification', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('From_Where', models.CharField(blank=True, max_length=200, null=True)),
                ('Year_of_work', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
