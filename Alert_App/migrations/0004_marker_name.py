# Generated by Django 2.1.5 on 2019-01-29 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alert_App', '0003_auto_20190128_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
