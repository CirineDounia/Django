# Generated by Django 4.0.1 on 2022-01-23 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0002_jury'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jury',
            name='codeJ',
            field=models.CharField(max_length=15),
        ),
    ]
