# Generated by Django 3.1 on 2020-09-28 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20200928_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='a',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app01.student'),
        ),
    ]