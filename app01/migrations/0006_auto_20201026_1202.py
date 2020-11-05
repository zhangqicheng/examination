# Generated by Django 3.1 on 2020-10-26 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
        ('app01', '0005_userprofile_roles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='roles',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rbac.role'),
        ),
    ]
