from django.db import models

# Create your models here.
Sex=(
        ('男','男'),
        ('女','女'),
        ('中性','中性')
    )
Dept=(
    ('计算机与通信学院', '计算机与通信学院'),
    ('电气与自动化学院', '电气与自动化学院'),
    ('外国语学院', '外国语学院'),
    ('理学院', '理学院'),
    ('土木工程学院','土木工程学院'),
)

#学院信息表
class Institute(models.Model):
    name=models.CharField('学院名称',max_length=64)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name='学院信息表'
        verbose_name_plural=verbose_name
        db_table='institute'
        unique_together=(
            ('name',)
        )

#专业信息表
class Profession(models.Model):
    iid=models.ForeignKey(name='学院名称',to=Institute,on_delete=models.CASCADE)
    career=models.CharField('专业名称',max_length=64)

    def __str__(self):
        return self.career

    class Meta():
        verbose_name='专业信息表'
        verbose_name_plural=verbose_name
        db_table='profession'
        unique_together=(
            ('career',)
        )

#学生表
class Student(models.Model):
    id=models.CharField('学号',max_length=16,primary_key=True)
    name=models.CharField('姓名',max_length=16)
    sex=models.CharField('性别',max_length=8,choices=Sex,default='中性')
    # academy=models.CharField('所在学院',max_length=32,choices=Dept)
    # profession=models.CharField('专业',max_length=64)
    academy=models.ForeignKey(name='所在学院',to=Institute,on_delete=models.CASCADE,default='')
    profession=models.ForeignKey(name='所在专业',to=Profession,on_delete=models.CASCADE,default='')
    password=models.CharField('密码',max_length=24,default='123')
    email=models.EmailField('邮箱',default=None)
    birth=models.DateField('出生日期')

    def __str__(self):
        return self.name+':'+self.id

    class Meta():
        verbose_name='学生表'
        verbose_name_plural=verbose_name
        db_table='student'

#教师表
class Teacher(models.Model):
    id=models.CharField('教工号',max_length=16,primary_key=True)
    name=models.CharField('姓名',max_length=16)
    sex=models.CharField('性别',max_length=8,choices=Sex)
    academy = models.CharField('所在学院', max_length=32, choices=Dept)
    password = models.CharField('密码', max_length=24, default='123')
    email = models.EmailField('邮箱', default=None)
    birth = models.DateField('出生日期')

    def __str__(self):
        return self.name + ':' + self.id

    class Meta():
        verbose_name = '教师表'
        verbose_name_plural = verbose_name
        db_table = 'teacher'

#单项选择表
class QuestionSingle(models.Model):
    ANSWER=(
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D'),
    )
    LEVEL=(
        ('1','easy'),
        ('2','common'),
        ('3','difficult'),
    )
    id=models.AutoField(primary_key=True)
    subject=models.CharField('科目',max_length=20)
    title=models.TextField('题目')
    optionA=models.CharField('A选项',max_length=30)
    optionB = models.CharField('B选项', max_length=30)
    optionC = models.CharField('C选项', max_length=30)
    optionD = models.CharField('D选项', max_length=30)
    answer=models.CharField('答案',max_length=10,choices=ANSWER)
    level=models.CharField('等级难度',max_length=16,choices=LEVEL)
    score=models.IntegerField('分数')

    def __str__(self):
        return str(self.id)

    class Meta():
        verbose_name = '单项选择表'
        verbose_name_plural = verbose_name
        db_table = 'questionsingle'

#成绩表
class Grade(models.Model):
    # id=models.CharField('id',max_length=16,primary_key=True,auto_created=True)
    sid=models.ForeignKey(name='学生',to=Student,on_delete=models.CASCADE,default='')
    subject=models.CharField('科目',max_length=20)
    grade=models.IntegerField()

    def __str__(self):
        return self.subject+':'+self.sid.name

    class Meta():
        verbose_name = '成绩表'
        verbose_name_plural = verbose_name
        db_table = 'grade'

#教师组卷表
class Paper(models.Model):
    # pid=models.ManyToManyField(name='单项选择',to=QuestionSingle,db_table='paper_pid')   #多对多
    # tid=models.ForeignKey(name='所属教师',to=Teacher,on_delete=models.CASCADE,default='')
    pid = models.ManyToManyField(to=QuestionSingle, db_table='paper_pid')  # 多对多
    tid = models.ForeignKey(to=Teacher, on_delete=models.CASCADE, default='')

    subject=models.CharField('科目',max_length=64)
    profession=models.CharField('试卷适用专业',max_length=64)
    examtime=models.DateTimeField('考试时间')

    def __str__(self):
        return self.subject

    class Meta():
        verbose_name = '试卷'
        verbose_name_plural = verbose_name
        db_table = 'paper'




















