# Generated by Django 2.1.5 on 2019-01-30 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alert_App', '0007_auto_20190129_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
