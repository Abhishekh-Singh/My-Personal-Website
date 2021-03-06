# Generated by Django 4.0.1 on 2022-04-03 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0034_alter_skill_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('Photo', models.ImageField(default='images/about.jpg', null=True, upload_to='images')),
                ('title1', models.CharField(blank=True, max_length=200, null=True)),
                ('description1', models.CharField(blank=True, max_length=200, null=True)),
                ('title2', models.CharField(blank=True, max_length=200, null=True)),
                ('description2', models.CharField(blank=True, max_length=200, null=True)),
                ('title3', models.CharField(blank=True, max_length=200, null=True)),
                ('description3', models.CharField(blank=True, max_length=200, null=True)),
                ('resume', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('sub_title', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Endorsement',
        ),
        migrations.DeleteModel(
            name='Qualification',
        ),
        migrations.DeleteModel(
            name='Work',
        ),
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(default='/images/placeholder.png', null=True, upload_to='images'),
        ),
    ]
