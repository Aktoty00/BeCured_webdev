# Generated by Django 2.2 on 2019-04-26 10:42

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='patient_diagnosis',
            field=models.CharField(default='', max_length=200),
        ),
    ]
