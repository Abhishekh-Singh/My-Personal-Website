# Generated by Django 4.0.1 on 2022-02-01 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_alter_project_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(blank=True, default='/images/default.jpg', null=True, upload_to=''),
        ),
    ]
