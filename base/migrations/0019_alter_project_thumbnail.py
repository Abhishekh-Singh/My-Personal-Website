# Generated by Django 4.0.1 on 2022-02-01 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_alter_project_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]