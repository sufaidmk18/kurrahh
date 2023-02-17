from multiprocessing import context
from tracemalloc import Statistic
from django.shortcuts import render
from django.http import HttpResponse
from .form import StudentForm
from .models import Student , Statistics,Attendence,Coach
# Create your views here.
def attendence(request):
    context={
        'title':"Attendence",
    }
    options=[{"name":'today',"link":"today"},{"name":"total","link":"total"}]
    context['options']=options
    return render(request,"common.html" ,context=context)

def total(request):
    context={"title":"total attendence"}
    
    return render(request,"table.html",context=context)

def today(request):
    context={"title":"total attendence"}
    c=Coach.objects.get(user_id=request.user.id)
    context['student']=Student.objects.filter(coach=c)
    return render(request,"table.html",context=context)

def addstudent(request):
    context={}
    if request.method == "POST":
        form = StudentForm(request.POST)  
        if form.is_valid():  
            form.save() 
            context["forms"]=StudentForm()
            context["m"]=True
            return render(request,'forms.html',context=context)
    context["forms"]=StudentForm()
    return render(request,'forms.html',context=context)

def studentlist(request):
    c=Coach.objects.get(user_id=request.user.id)
    context={}
    context['title']="Student"
    context['student']=Student.objects.filter(coach=c)
    return render(request,"studlist.html",context=context)
def studentdetails(request,id):
    context={}
    stu=Student.objects.get(id=id)
    context['title']=stu.name
    context['forms']=StudentForm(instance=stu)
    return render(request,"forms.html",context=context)
def studentmenu(request,id):
    context={}
    context['id']=id
    return render(request,"smenu.html",context=context)
def statistics(request,id):
    if Statistics.objects.filter(Student_id=id).exists():
        print(Statistics.objects.filter(Student_id=id).exists)
    else:
        s=Statistics.objects.create(Student_id=id)
        s.save()
    context={}
    context["s"]=Statistics.objects.get(Student_id=id)
    context["id"]=id
    return render(request,"statistics.html",context=context)

def changestatics(request,id,attri,val):
    s=Statistics.objects.get(Student_id=id)
    if attri is 1:
        s.speed=val
    elif attri is 2:
        s.stamina=val
    elif attri is 3:
        s.bollcontronl=val
    elif attri is 4:
        s.passaccuracy=val
    elif attri is 5:
        s.shoot=val
    elif attri is 6:
        s.takles = val
    s.save()
    return HttpResponse("good")

def add_attendence(request,id,val,date):
    if Attendence.objects.filter(Student_id=id,date=date).exists():
        a=Attendence.objects.get(Student_id=id,date=date)
        a.present=val
        a.save()
        return HttpResponse("changed")
    else :
        Attendence.objects.get(Student_id=id,date=date,present=val).save()
        return HttpResponse("created")

    