# Generated by Django 3.2.14 on 2022-09-26 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
