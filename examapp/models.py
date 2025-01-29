from django.db import models

# Create your models here.

class Question(models.Model):
    
    qno=models.IntegerField(primary_key=True)
    qtext=models.CharField(max_length=100)
    answer=models.CharField(max_length=50)
    op1=models.CharField(max_length=50)
    op2=models.CharField(max_length=50)
    op3=models.CharField(max_length=50)
    op4=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)

    def __str__(self):
        return f"qno={self.qno} , qtext={self.qtext},answer={self.answer},op1={self.op1},op2={self.op2},op3={self.op3},op4={self.op4},subject={self.subject}"
    
    class Meta:
        db_table="question"


class Result(models.Model):

    username=models.CharField(max_length=50,primary_key=True)

    subject=models.CharField(max_length=70)

    score=models.IntegerField()
    

class Meta:
        db_table="result"