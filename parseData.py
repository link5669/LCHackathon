from django.db import models
from django.db.models import Model

class Student(models.Model):
    studentUName = models.CharField(max_length=16)
    studentPassword = models.CharField(max_length=16)
    studentDS = models.BooleanField()
    studentExpos = models.BooleanField()


def studentinfo(request):
    stud = Student.objects.all()
    print("Myoutput",stud)
    return render(request,'userHome.html',{'stu': stud})
