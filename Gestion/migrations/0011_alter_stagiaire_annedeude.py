# Generated by Django 4.0.1 on 2022-01-24 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0010_ficheeva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stagiaire',
            name='annedEude',
            field=models.CharField(choices=[('1CPI', '1CPI'), ('1CS', '1CS'), ('PFE3CS', '3CS')], max_length=20),
        ),
    ]