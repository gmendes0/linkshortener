# Generated by Django 3.0.8 on 2020-07-18 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='clicks',
            field=models.IntegerField(default=0),
        ),
    ]