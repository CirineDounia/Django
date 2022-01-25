# Generated by Django 4.0.1 on 2022-01-24 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0008_stagiaire'),
    ]

    operations = [
        migrations.CreateModel(
            name='Convention',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duree', models.CharField(max_length=2)),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.stage')),
            ],
        ),
    ]