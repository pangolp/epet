# Generated by Django 2.2 on 2019-04-23 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_auto_20190423_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libreta',
            name='localidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='agenda.Localidad'),
        ),
        migrations.AlterField(
            model_name='libreta',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='agenda.Provincia'),
        ),
    ]
