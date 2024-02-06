from django.shortcuts import render,redirect
from Testapp.models import Student
from Testapp.forms import StudentModelForm

# Create your views here.
def getdata_view(request):
    stu=Student.objects.all()
    return render(request,'testapp/result.html',{'STU':stu})

def insert_view(request): 
    frm=StudentModelForm()    
    if request.method=="POST":       
        frm=StudentModelForm(request.POST)
        if frm.is_valid():
            frm.save()
        return redirect("/")
    return render(request,'testapp/insert.html',{'FRM':frm})

def  delete_view(request,id):
   stu=Student.objects.get(id=id)
   stu.delete()
   return redirect("/")

def update_view(request,id):
    stu=Student.objects.get(id=id) #6
    #stu=Select * from student where id=6;
    frm=StudentModelForm(instance=stu)
    if request.method=="POST":
        frm=StudentModelForm(request.POST,instance=stu)
        if frm.is_valid():
           frm.save()        
        return redirect("/")
    return render(request,'testapp/update.html',{'FRM':frm})

