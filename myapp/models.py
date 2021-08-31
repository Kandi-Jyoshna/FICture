from django.db import models
# Create your models here.
class ClassC3(models.Model):
    rollno=models.IntegerField('Roll No')
    name=models.CharField(max_length=300)
    section=models.IntegerField('section')
    surname=models.CharField(max_length=300)
    address=models.CharField(max_length=300)
    def __str__(self):
        return self.rollno

class Faculty(models.Model):
    name=models.CharField(max_length=300)
    emailid=models.EmailField(max_length=300)

class Form(models.Model):
    name=models.CharField(max_length=300)
    rollnumber=models.IntegerField('Roll number')
    objectname=models.CharField(max_length=300)
    place=models.CharField(max_length=300)
    description=models.TextField()
    contact=models.CharField('Contact No',max_length=10)
    pub_date=models.DateField()

class AskHelp(models.Model):
    nameField=models.CharField(max_length=300)
    roll=models.IntegerField()
    objectlost=models.CharField(max_length=300)
    describe=models.TextField()
    contactdetails=models.CharField(max_length=10)
    post_date=models.DateField()

class college(models.Model):
    code=models.IntegerField()
    name=models.CharField(max_length=300)

