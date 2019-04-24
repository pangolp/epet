# Generated by Django 2.2 on 2019-04-24 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_cargo_institucional'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='institucional',
            options={'ordering': ['cargo'], 'verbose_name': 'institucional', 'verbose_name_plural': 'autoridades'},
        ),
        migrations.AlterField(
            model_name='institucional',
            name='foto',
            field=models.ImageField(default='institucional/perfil/no-img.png', upload_to='institucional/perfil'),
        ),
    ]
