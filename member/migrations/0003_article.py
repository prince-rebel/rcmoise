# Generated by Django 4.1.3 on 2022-11-28 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_rename_profile_type_membre_type_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=200, verbose_name='Designation')),
                ('qte', models.FloatField(verbose_name='Quantité')),
                ('Prix_unitaire', models.FloatField(verbose_name='Prix U')),
                ('Prix_total', models.FloatField(verbose_name='Prix T')),
            ],
        ),
    ]
