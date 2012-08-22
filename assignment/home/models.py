from django.db import models


class Teacher(models.Model):
    DEPARTMENT = (
        ('CS', 'Computer Sci'),
        ('ECE', 'Electronics'),
        ('MAE', 'Mechanical'),
        ('Civil', 'Computer Sci'),
        ('Biotech', 'BioTech'),
            )
    tname = models.CharField(max_length=60)
    dept = models.CharField(max_length=15, choices=DEPARTMENT)
    email=models.EmailField(blank=True, verbose_name='e-mail')

    def __unicode__(self):
        return self.tname

class Course(models.Model):
    NAME_CHOICES = (
        ('B.Tech CSE', 'B.Tech Computer Science'),
        ('B.Tech Aeronautics', 'B.Tech Aeronautics'),
        ('B.Tech Electrical', 'B.Tech Electrical'),
        ('B.Tech MAE', 'B.Tech Mechanical and Automation'),
        ('B.Tech Civil', 'B.Tech Civil'),
        ('B.Tech ECE', 'B.Tech Electronics and Communication'),
        ('BBA', 'BBA'),
        ('B.Com', 'B.Com'),
        ('B.SC IT', 'B.Sc IT'),
        ('B.Sc Nursing', 'B.Sc Nursing'),
            )
    SESSION_CHOICES = zip(range(2010,2020), range(2010,2020))
    cname = models.CharField(max_length=50, choices = NAME_CHOICES)
    session_start = models.IntegerField(choices=SESSION_CHOICES)
    session_end = models.IntegerField(choices=SESSION_CHOICES)

    class Meta:
        unique_together = ("cname", "session_start", "session_end")

    def __unicode__(self):
        return self.cname

class Subject(models.Model):
    sname = models.CharField(max_length=60)
    course = models.ForeignKey(Course)
    teacher = models.ForeignKey(Teacher)

    def __unicode__(self):
        return self.sname

class Assignment(models.Model):
    aname = models.CharField(max_length=60)
    subject = models.ForeignKey(Subject)
    publication_date = models.DateField(null=True)
    last_submission_date = models.DateField(null=True)

    def __unicode__(self):
        return self.aname

class Question(models.Model):
    qname = models.CharField(max_length=200)
    assignment = models.ForeignKey(Assignment)

    def __unicode__(self):
        return self.qname


class Student(models.Model):
    student_name = models.CharField(max_length=60)
    course = models.ForeignKey(Course)
    email=models.EmailField(blank=True, verbose_name='e-mail')

    def __unicode__(self):
        return self.student_name

class Answer(models.Model):
    question = models.ForeignKey(Question)
    content = models.TextField()
    student = models.ForeignKey(Student)
    submission_date = models.DateField(null=True)

    def __unicode__(self):
        return self.content
