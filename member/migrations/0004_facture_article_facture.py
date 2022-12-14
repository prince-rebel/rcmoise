# Generated by Django 4.1.3 on 2022-11-28 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Num_Fact', models.CharField(max_length=200, verbose_name='N Facture')),
                ('Total', models.FloatField(verbose_name='Total')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='Facture',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to='member.facture'),
            preserve_default=False,
        ),
    ]
