from django.db import models

class Studentresult(models.Model):
    #id = models.AutoField()
    stu_name = models.CharField(max_length=200)
    rollno = models.PositiveIntegerField()
    parents_name = models.CharField(max_length=200)
    mo = models.PositiveBigIntegerField()
    total_subjects = models.PositiveIntegerField()
    results = models.FloatField()
    grd = models.CharField(max_length=10)
    