# Generated by Django 2.1.5 on 2019-01-30 16:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Alert_App', '0010_auto_20190130_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]