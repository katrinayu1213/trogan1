# Generated by Django 3.0.8 on 2020-08-16 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200816_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encounter',
            name='Gen_Med',
        ),
        migrations.RemoveField(
            model_name='encounter',
            name='Gen_PT',
        ),
    ]