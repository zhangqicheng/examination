# Generated by Django 3.1 on 2020-10-29 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_questionsubjective_remark'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='subjective',
            field=models.ManyToManyField(to='teacher.QuestionSubjective', verbose_name='多项选择'),
        ),
    ]
