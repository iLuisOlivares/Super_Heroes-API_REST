# Generated by Django 3.2.4 on 2023-06-23 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_character_superhero_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='id',
        ),
        migrations.AlterField(
            model_name='character',
            name='superhero_name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
