# Generated by Django 2.2 on 2019-04-24 19:00

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Request',
            new_name='Rrequest',
        ),
        migrations.RenameModel(
            old_name='Response',
            new_name='Rresponse',
        ),
        migrations.AddField(
            model_name='doctor',
            name='patient_diagnosis',
            field=models.CharField(default='I10', max_length=200),
        ),
        migrations.AlterField(
            model_name='patient',
            name='diagnosis',
            field=models.CharField(default='I10', max_length=200),
        ),
    ]
