# Generated by Django 2.1.5 on 2019-01-30 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alert_App', '0008_auto_20190129_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]