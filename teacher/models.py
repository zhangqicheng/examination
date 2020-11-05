from django.db import models
import app01
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

#教师表
# class Teacher(Student):
    # id=models.CharField(verbose_name='教工号',max_length=16,primary_key=True)
    # name=models.CharField(verbose_name='姓名',max_length=16)
    # sex=models.CharField(verbose_name='性别',max_length=8,choices=Sex)
    # academy = models.CharField(verbose_name='所在学院', max_length=32, choices=Dept)
    # password = models.CharField(verbose_name='密码', max_length=24, default='123')
    # email = models.EmailField(verbose_name='邮箱', default=None)
    # birth = models.DateField(verbose_name='出生日期')

    # def __str__(self):
    #     return self.name
    #
    # class Meta():
    #     verbose_name = '教师表'
    #     verbose_name_plural = verbose_name
    #     db_table = 'teacher'

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
    subject=models.CharField(verbose_name='科目',max_length=20)
    title=models.TextField(verbose_name='题目')
    optionA=models.CharField(verbose_name='A选项',max_length=30)
    optionB = models.CharField(verbose_name='B选项', max_length=30)
    optionC = models.CharField(verbose_name='C选项', max_length=30)
    optionD = models.CharField(verbose_name='D选项', max_length=30)
    answer=models.CharField(verbose_name='答案',max_length=10,choices=ANSWER)
    level=models.CharField(verbose_name='等级难度',max_length=16,choices=LEVEL)
    score=models.IntegerField(verbose_name='分数')

    def __str__(self):
        # return str(self.id)
        return self.title

    class Meta():
        verbose_name = '单项选择题'
        verbose_name_plural = verbose_name
        db_table = 'questionsingle'

#主观题
class QuestionSubjective(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(verbose_name='科目', max_length=20)
    title = models.TextField(verbose_name='题目')
    answer = models.TextField(verbose_name='参考答案',null=True)
    score = models.IntegerField(verbose_name='分数')
    remark=models.CharField(verbose_name='备注',max_length=64,null=True)

    def __str__(self):
        # return str(self.id)
        return self.title

    class Meta():
        verbose_name = '主观题'
        verbose_name_plural = verbose_name
        db_table = 'questionsubjective'

#教师组卷表
class Paper(models.Model):
    pid = models.ManyToManyField(verbose_name='单项选择',to=QuestionSingle)  # 多对多
    subjective=models.ManyToManyField(verbose_name='多项选择',to=QuestionSubjective)  #多对多
    tid = models.ForeignKey(verbose_name='所属教师',to="app01.UserProfile", on_delete=models.CASCADE, default='')
    subject=models.CharField(verbose_name='科目',max_length=64)
    profession=models.CharField(verbose_name='试卷适用专业',max_length=64)
    examtime=models.DateTimeField(verbose_name='考试时间')
    status=models.CharField(verbose_name='状态',max_length=16,choices=(('1','正在进行'),('2','已关闭')),default='1')

    def __str__(self):
        return self.subject

    class Meta():
        verbose_name = '试卷'
        verbose_name_plural = verbose_name
        db_table = 'paper'