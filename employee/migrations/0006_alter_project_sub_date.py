# Generated by Django 4.1.4 on 2022-12-17 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_alter_project_sub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='sub_date',
            field=models.DateField(null=True),
        ),
    ]
