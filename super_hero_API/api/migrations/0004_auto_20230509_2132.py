# Generated by Django 3.2.4 on 2023-05-09 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_superhero_publisher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='name',
        ),
        migrations.AddField(
            model_name='location',
            name='description',
            field=models.TextField(default='n'),
            preserve_default=False,
        ),
    ]