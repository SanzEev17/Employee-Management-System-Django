# Generated by Django 4.1.4 on 2022-12-17 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='sub_date',
            field=models.DateField(default=None, null=True),
        ),
    ]
