# Generated by Django 3.2.4 on 2023-05-09 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20230508_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superhero',
            name='publisher',
            field=models.CharField(max_length=15),
        ),
    ]