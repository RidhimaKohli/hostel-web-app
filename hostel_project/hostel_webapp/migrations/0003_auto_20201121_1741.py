# Generated by Django 3.0.8 on 2020-11-21 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_webapp', '0002_complaint_hostel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='hostel',
            field=models.CharField(choices=[('B1', 'B1'), ('B2', 'B2'), ('B3', 'B3'), ('B4', 'B5'), ('G1', 'G1'), ('G2', 'G2'), ('G3', 'G3'), ('G4', 'G4'), ('G5', 'G5'), ('G6', 'G6'), ('I2', 'I2')], default='B1', max_length=2),
        ),
    ]
