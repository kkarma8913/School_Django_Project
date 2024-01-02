from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.db.models import Q


def sign_up(request):
    if request.method == 'POST':
        myform = CustomerRegistrationForm(request.POST)
        if myform.is_valid():
            myform.save()
            msgs='Congratulations!! Registered Successfully.'
            myform = CustomerRegistrationForm()
            return render(request,'signup.html',{'myform':myform,'msgs':msgs})
        else:
            msge= 'Something wrong'
            myform = CustomerRegistrationForm()
            return render(request,'signup.html',{'myform':myform,'msge':msge})   
    else:
        myform =    CustomerRegistrationForm()
        return render(request,'signup.html',{'myform':myform})


def log_in(request):
    if request.method == "POST":
        myform = LoginForm(request=request,data=request.POST)
        if myform.is_valid():
            uname=myform.cleaned_data['username']
            upass= myform.cleaned_data['password']

            request.session['uname']=uname
            user = authenticate(username=uname,password=upass)
            login(request,user)
            return redirect('home')
        else:
            msg = "username or password is incorrect"
            myform = LoginForm()
            return render(request,'login.html',{'myform':myform,'msge':msg})    
    else:
        myform = LoginForm()
        return render(request,'login.html',{'myform':myform})




def log_out(request):
    logout(request)
    return redirect('login')        





# Create your views here.

def home(request):
     return render(request,'home.html')

def about(request):
     return render(request,'about.html') 

       

def feestr(request):
     return render(request,'feestr.html')       


    
def nco(request):
     return render(request,'nco.html') 

def kg1(request):
     return render(request,'K.G.I.html')  
    
   
def kg2(request):
     return render(request,'K.G.II.html')

def ttpg(request):
     return render(request,'ttpg.html')     
     
def do(request):
     return render(request,'do.html')

def feed(request):
     return render(request,'feed.html')


def show_img(request):
     obj=img.objects.all()
     return render(request,'img.html',{'obj':obj})


def applyad(request):
    if request.method == 'POST':
        myform= admissionform(request.POST, request.FILES)
        if myform.is_valid():
            myform.save()
            messages.success(request,"Form submitted")
            myform=admissionform()
        return render(request,'applyad.html',{'form':myform})
       

    else:
        myform=admissionform()
        return render(request,'applyad.html',{'form':myform})    

def feed(request):
    if request.method == 'POST':
        myform=feedbackform(request.POST)
        if myform.is_valid():
            myform.save()
            messages.success(request,"Form submitted")
            myform=feedbackform()
        return render(request,'feed.html',{'form':myform})
       

    else:
        myform=feedbackform()
        return render(request,'feed.html',{'form':myform}) 
        

def contact(request):
    if request.method == 'POST':
        myform=contactform(request.POST)
        if myform.is_valid():
            myform.save()
            messages.success(request,"Form submitted")
            myform=contactform()
        return render(request,'contact.html',{'form':myform})
    else:
        myform=contactform()
        return render(request,'contact.html',{'form':myform})
    
def show_fees(request):
    data=CommonFees.objects.all()
    data1=fees.objects.all() 
    y=[]
    for i in data1:
        x=i.inst1+i.inst2+i.inst3+i.inst4
        y.append(x)

       

    return render(request,'feestr.html',{'data':data,'data1':data1,'y':y}) 

  

def show_plyg(request):
       pg=playg.objects.get(name='Playgroup')
       playgroup=course_g.objects.filter(play_g=pg)

       nr=playg.objects.get(name='nursery')
       nursery= course_g.objects.filter(play_g=nr)

       kg_1=playg.objects.get(name='kg1')
       kg1= course_g.objects.filter(play_g=kg_1)

       kg_2=playg.objects.get(name='kg2')
       kg2= course_g.objects.filter(play_g=kg_2)


       data =playg.objects.all()
       return render(request,'pgc.html',{'data':data,'playgroup':playgroup,'nursery':nursery,'kg1':kg1,'kg2':kg2})

def show_tt_play(request):
    data = time_slot.objects.all()
    gp_data=playg.objects.all()

    ply_data_mon_list=[]
    ply_data_tue_list=[]
    ply_data_wed_list=[]
    ply_data_thu_list=[]
    ply_data_fri_list=[]
    for i in data:
        plg_data=timetable.objects.filter(Q(group_name=gp_data[0]) & Q(days='Monday') & Q(timing=i))
        if plg_data:
            ply_data_mon_list.append(plg_data[0])
        else:
            ply_data_mon_list.append("")

    for i in data:
        plg_data=timetable.objects.filter(Q(group_name=gp_data[0]) & Q(days='Tuesday') & Q(timing=i))
        if plg_data:
            ply_data_tue_list.append(plg_data[0])
        else:
            ply_data_tue_list.append("a")
              
    for i in data:
        plg_data=timetable.objects.filter(Q(group_name=gp_data[0]) & Q(days='Wednesday') & Q(timing=i))
        if plg_data:
            ply_data_wed_list.append(plg_data[0])
        else:
            ply_data_wed_list.append("a")
    for i in data:
        plg_data=timetable.objects.filter(Q(group_name=gp_data[0]) & Q(days='Thrusday') & Q(timing=i))
        if plg_data:
            ply_data_thu_list.append(plg_data[0])
        else:
            ply_data_thu_list.append("a")
    for i in data:
        plg_data=timetable.objects.filter(Q(group_name=gp_data[0]) & Q(days='Friday') & Q(timing=i))
        if plg_data:
            ply_data_fri_list.append(plg_data[0])
        else:
            ply_data_fri_list.append("a")

    nus_data_mon_list=[]
    nus_data_tue_list=[]
    nus_data_wed_list=[]
    nus_data_thu_list=[]
    nus_data_fri_list=[]
    for i in data:
        nus_data=timetable.objects.filter(Q(group_name=gp_data[1]) & Q(days='Monday') & Q(timing=i))
        if nus_data:
            nus_data_mon_list.append(nus_data[0])
        else:
            nus_data_mon_list.append("a")        
    for i in data:
        nus_data=timetable.objects.filter(Q(group_name=gp_data[1]) & Q(days='Tuesday') & Q(timing=i))
        if nus_data:
            nus_data_tue_list.append(nus_data[0])
        else:
            nus_data_tue_list.append("a") 
    for i in data:
        nus_data=timetable.objects.filter(Q(group_name=gp_data[1]) & Q(days='Wednesday') & Q(timing=i))
        if nus_data:
            nus_data_wed_list.append(nus_data[0])
        else:
            nus_data_wed_list.append("a") 
    for i in data:
        nus_data=timetable.objects.filter(Q(group_name=gp_data[1]) & Q(days='Thrusday') & Q(timing=i))
        if nus_data:
            nus_data_thu_list.append(nus_data[0])
        else:
            nus_data_thu_list.append("a") 
    for i in data:
        nus_data=timetable.objects.filter(Q(group_name=gp_data[1]) & Q(days='Friday') & Q(timing=i))
        if nus_data:
            nus_data_fri_list.append(nus_data[0])
        else:
            nus_data_fri_list.append("a")    

    kg1_data_mon_list=[]
    kg1_data_tue_list=[]
    kg1_data_wed_list=[]
    kg1_data_thu_list=[]
    kg1_data_fri_list=[]
    for i in data:
        kg1_data=timetable.objects.filter(Q(group_name=gp_data[2]) & Q(days='Monday') & Q(timing=i))
        if kg1_data:
            kg1_data_mon_list.append(kg1_data[0])
        else:
            kg1_data_mon_list.append("a") 
    for i in data:
        kg1_data=timetable.objects.filter(Q(group_name=gp_data[2]) & Q(days='Tuesday') & Q(timing=i))
        if kg1_data:
            kg1_data_tue_list.append(kg1_data[0])
        else:
            kg1_data_tue_list.append("a") 
    for i in data:
        kg1_data=timetable.objects.filter(Q(group_name=gp_data[2]) & Q(days='Wednesday') & Q(timing=i))
        if kg1_data:
            kg1_data_wed_list.append(kg1_data[0])
        else:
            kg1_data_wed_list.append("a") 
    for i in data:
        kg1_data=timetable.objects.filter(Q(group_name=gp_data[2]) & Q(days='Thrusday') & Q(timing=i))
        if kg1_data:
            kg1_data_thu_list.append(kg1_data[0])
        else:
            kg1_data_thu_list.append("a") 
    for i in data:
        kg1_data=timetable.objects.filter(Q(group_name=gp_data[2]) & Q(days='Friday') & Q(timing=i))
        if kg1_data:
            kg1_data_fri_list.append(kg1_data[0])
        else:
            kg1_data_fri_list.append("a") 

    kg2_data_mon_list=[]
    kg2_data_tue_list=[]
    kg2_data_wed_list=[]
    kg2_data_thu_list=[]
    kg2_data_fri_list=[]
    for i in data:
        kg2_data=timetable.objects.filter(Q(group_name=gp_data[3]) & Q(days='Monday') & Q(timing=i))
        if kg2_data:
            kg2_data_mon_list.append(kg2_data[0])
        else:
            kg2_data_mon_list.append("a")
    for i in data:
        kg2_data=timetable.objects.filter(Q(group_name=gp_data[3]) & Q(days='Tuesday') & Q(timing=i))
        if kg2_data:
            kg2_data_tue_list.append(kg2_data[0])
        else:
            kg2_data_tue_list.append("a")
    for i in data:
        kg2_data=timetable.objects.filter(Q(group_name=gp_data[3]) & Q(days='Wednesday') & Q(timing=i))
        if kg2_data:
            kg2_data_wed_list.append(kg2_data[0])
        else:
            kg2_data_wed_list.append("a")        
    for i in data:
        kg2_data=timetable.objects.filter(Q(group_name=gp_data[3]) & Q(days='Thrusday') & Q(timing=i))
        if kg2_data:
            kg2_data_thu_list.append(kg2_data[0])
        else:
            kg2_data_thu_list.append("a")
    for i in data:
        kg2_data=timetable.objects.filter(Q(group_name=gp_data[3]) & Q(days='Friday') & Q(timing=i))
        if kg2_data:
            kg2_data_fri_list.append(kg2_data[0])
        else:
            kg2_data_fri_list.append("a")                   

    context= {'data':data,'pl_mon':ply_data_mon_list,'pl_tue':ply_data_tue_list,'pl_wed':ply_data_wed_list,'pl_thu':ply_data_thu_list,'pl_fri':ply_data_fri_list,'nus_mon':nus_data_mon_list,'nus_tue':nus_data_tue_list,'nus_wed':nus_data_wed_list,'nus_thu':nus_data_thu_list,'nus_fri':nus_data_fri_list,'kg1_mon':kg1_data_mon_list,'kg1_tue':kg1_data_tue_list,'kg1_wed':kg1_data_wed_list,'kg1_thu':kg1_data_thu_list,'kg1_fri':kg1_data_fri_list,'kg2_mon':kg2_data_mon_list,'kg2_tue':kg2_data_tue_list,'kg2_wed':kg2_data_wed_list,'kg2_thu':kg2_data_thu_list,'kg2_fri':kg2_data_fri_list} 
                 
    return render(request,'timetable.html',context)


















# def add_user(request):
#     if request.method =='POST':
#         myform=user(request.POST)
#         if   myform.is_valid():
#              myform.save()
#              return HttpResponse("<h1>Add the user information</h1>")
#         else:
#              myform=user()
#              return render(request,'adduser.html',{'myform':myform})
#     else:
#            return render(request,'adduser.html')             
