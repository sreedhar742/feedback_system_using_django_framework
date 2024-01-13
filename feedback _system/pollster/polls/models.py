from django.db import models

# Create your models here.



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    

    def __str__(self):
        return self.choice_text







class Sir(models.Model):
    name=models.CharField(max_length=100)
    rollno=models.IntegerField(max_length=10)
    def __str__(self):
        return self.name

class Student(models.Model):
    student=models.CharField(("enter your name"),max_length=50)
    father=models.CharField(("enter your father name"), max_length=50)   
    mother=models.CharField(("enter your father name"), max_length=50)   
    def __str__(self):
        return self.student
    
    


class Registration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_name= models.CharField(max_length=100)
    gmail = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

