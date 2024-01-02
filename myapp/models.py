from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

admission_choices=[ ('Play Group','Play Group'),('nursery','nursery'),('K.G.I','K.G.I'),('K.G.II','K.G.II')]
days=[('Monday','Monday'),('Tuesday','Tuesday'),('Wednesday','Wednesday'),('Thrusday','Thrusday'),('Friday','Friday')]



class admission(models.Model):
    student_name=models.CharField(max_length=20,validators=[RegexValidator("[a-zA-Z][a-zA-Z ]+[a-zA-Z]$",message="Enter only Alphabets")])
    age=models.IntegerField()   
    date_of_birth=models.DateField()
    education=models.CharField(max_length=20)   
    admission_for=models.CharField(max_length=10,choices=admission_choices)
    father_name=models.CharField(max_length=20,validators=[RegexValidator("[a-zA-Z][a-zA-Z ]+[a-zA-Z]$",message="Enter only Alphabets")])  
    father_age=models.IntegerField()
    father_Contact_no=models.CharField(max_length=10,validators=[RegexValidator("^[0-9]*$",message="Enter only Numbers")])  
    father_qualification=models.CharField(max_length=50)
    father_occupation=models.CharField(max_length=20)
    mother_name=models.CharField(max_length=20,validators=[RegexValidator("[a-zA-Z][a-zA-Z ]+[a-zA-Z]$",message="Enter only Alphabets")])  
    mother_age=models.IntegerField() 
    mother_Contact_no=models.CharField(max_length=10,validators=[RegexValidator("^[0-9]*$",message="Enter only Numbers")])
    mother_qualification=models.CharField(max_length=50) 
    mother_occupation=models.CharField(max_length=20)    
    email=models.EmailField(max_length=30)  
    address=models.CharField(max_length=80) 
    caste_category=models.CharField(max_length=10)
    student_image=models.ImageField(upload_to='img')



    def __str__(self):
        return  str(self.student_name)


class feedback(models.Model):

    full_name=models.CharField(max_length=20,validators=[RegexValidator("[a-zA-Z][a-zA-Z ]+[a-zA-Z]$",message="Enter only Alphabets")])
    Contact_no=models.CharField(max_length=10,validators=[RegexValidator("^[0-9]*$",message="Enter only Numbers")])
    suggestion=models.CharField(max_length=200)
    remark=models.CharField(max_length=200)

    def __str__(self):
        return self.full_name

class contact_us(models.Model): 
    First_name=models.CharField(max_length=20,validators=[RegexValidator("[a-zA-Z][a-zA-Z ]+[a-zA-Z]$",message="Enter only Alphabets")])
    last_name=models.CharField(max_length=20,validators=[RegexValidator("[a-zA-Z][a-zA-Z ]+[a-zA-Z]$",message="Enter only Alphabets")])
    email=models.EmailField() 
    Contact_no=models.CharField(max_length=10,validators=[RegexValidator("^[0-9]*$",message="Enter only Numbers")]) 
    your_message=models.TextField()
     
    def __str__(self):
        return str(self.First_name)
    

class CommonFees(models.Model):
    admission_form=models.PositiveIntegerField()
    admission_fees=models.PositiveIntegerField()
    caution_money=models.PositiveIntegerField()
    id_card=models.PositiveIntegerField()
    transport=models.PositiveIntegerField()

    def __str__(self):
        return str(self.admission_form)
    
class fees(models.Model):
    group= models.CharField(max_length=10,choices=admission_choices)   
    inst1=models.PositiveIntegerField() 
    inst2=models.PositiveIntegerField() 
    inst3=models.PositiveIntegerField() 
    inst4=models.PositiveIntegerField() 
    total=models.PositiveIntegerField(editable=False)
    

    def __str__(self):
        return str(self.group)
    def save(self,*args,**kwargs):
        self.total=self.inst1+self.inst2+self.inst3+self.inst4 
        super(fees,self).save(*args,**kwargs)


            
class img(models.Model):
   student_images=models.ImageField(upload_to='img')

def __str__(self):
        return str(self.id)





class playg(models.Model):
    name=models.CharField(max_length=20,validators=[RegexValidator("^[a-zA-Z]*$",message="Enter only Alphabets")])

    def __str__(self):
        return self.name


class course_g(models.Model):
    play_g= models.ForeignKey(playg,on_delete=models.CASCADE)  
    coures_name=models.CharField(max_length=20)  

    def __str__(self):
        return self.coures_name
    

class time_slot(models.Model):
    time=models.CharField(max_length=10)

    def __str__(self):
        return self.time

class timetable(models.Model):
    group_name=models.ForeignKey(playg,on_delete=models.CASCADE) 
    days= models.CharField(max_length=10,choices=days)  
    timing=models.ForeignKey(time_slot,on_delete=models.CASCADE)
    content=models.CharField(max_length=50)

    def __str__(self):
        return self.group_name.name
    




  