# Generated by Django 2.2.3 on 2019-07-08 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_auto_20190708_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
