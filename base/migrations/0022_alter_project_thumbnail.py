# Generated by Django 4.0.1 on 2022-02-01 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_alter_project_body_alter_project_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(default='images/default.jpg', null=True, upload_to=''),
        ),
    ]
