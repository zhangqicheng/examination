# Generated by Django 3.0.3 on 2020-10-12 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='学院名称')),
            ],
            options={
                'verbose_name': '学院信息表',
                'verbose_name_plural': '学院信息表',
                'db_table': 'institute',
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('career', models.CharField(max_length=64, verbose_name='专业名称')),
                ('iid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app01.Institute', verbose_name='学院名称')),
            ],
            options={
                'verbose_name': '专业信息表',
                'verbose_name_plural': '专业信息表',
                'db_table': 'profession',
                'unique_together': {('career',)},
            },
        ),
        migrations.CreateModel(
            name='QuestionSingle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=20, verbose_name='科目')),
                ('title', models.TextField(verbose_name='题目')),
                ('optionA', models.CharField(max_length=30, verbose_name='A选项')),
                ('optionB', models.CharField(max_length=30, verbose_name='B选项')),
                ('optionC', models.CharField(max_length=30, verbose_name='C选项')),
                ('optionD', models.CharField(max_length=30, verbose_name='D选项')),
                ('answer', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=10, verbose_name='答案')),
                ('level', models.CharField(choices=[('1', 'easy'), ('2', 'common'), ('3', 'difficult')], max_length=16, verbose_name='等级难度')),
                ('score', models.IntegerField(verbose_name='分数')),
            ],
            options={
                'verbose_name': '单项选择表',
                'verbose_name_plural': '单项选择表',
                'db_table': 'questionsingle',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.CharField(max_length=16, primary_key=True, serialize=False, verbose_name='教工号')),
                ('name', models.CharField(max_length=16, verbose_name='姓名')),
                ('sex', models.CharField(choices=[('男', '男'), ('女', '女'), ('中性', '中性')], max_length=8, verbose_name='性别')),
                ('academy', models.CharField(choices=[('计算机与通信学院', '计算机与通信学院'), ('电气与自动化学院', '电气与自动化学院'), ('外国语学院', '外国语学院'), ('理学院', '理学院'), ('土木工程学院', '土木工程学院')], max_length=32, verbose_name='所在学院')),
                ('password', models.CharField(default='123', max_length=24, verbose_name='密码')),
                ('email', models.EmailField(default=None, max_length=254, verbose_name='邮箱')),
                ('birth', models.DateField(verbose_name='出生日期')),
                ('roles', models.ManyToManyField(blank=True, to='rbac.Role', verbose_name='拥有的所有角色')),
            ],
            options={
                'verbose_name': '教师表',
                'verbose_name_plural': '教师表',
                'db_table': 'teacher',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.CharField(max_length=16, primary_key=True, serialize=False, verbose_name='学号')),
                ('name', models.CharField(max_length=16, verbose_name='姓名')),
                ('sex', models.CharField(choices=[('男', '男'), ('女', '女'), ('中性', '中性')], default='中性', max_length=8, verbose_name='性别')),
                ('password', models.CharField(default='123', max_length=24, verbose_name='密码')),
                ('email', models.EmailField(default=None, max_length=254, verbose_name='邮箱')),
                ('birth', models.DateField(verbose_name='出生日期')),
                ('academy', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app01.Institute', verbose_name='所在学院')),
                ('profession', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app01.Profession', verbose_name='所在专业')),
                ('roles', models.ManyToManyField(blank=True, to='rbac.Role', verbose_name='拥有的所有角色')),
            ],
            options={
                'verbose_name': '学生表',
                'verbose_name_plural': '学生表',
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=64, verbose_name='科目')),
                ('profession', models.CharField(max_length=64, verbose_name='试卷适用专业')),
                ('examtime', models.DateTimeField(verbose_name='考试时间')),
                ('pid', models.ManyToManyField(to='app01.QuestionSingle', verbose_name='单项选择')),
                ('tid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app01.Teacher', verbose_name='所属教师')),
            ],
            options={
                'verbose_name': '试卷',
                'verbose_name_plural': '试卷',
                'db_table': 'paper',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=20, verbose_name='科目')),
                ('grade', models.IntegerField(verbose_name='成绩')),
                ('sid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app01.Student', verbose_name='学生')),
            ],
            options={
                'verbose_name': '成绩表',
                'verbose_name_plural': '成绩表',
                'db_table': 'grade',
            },
        ),
    ]
