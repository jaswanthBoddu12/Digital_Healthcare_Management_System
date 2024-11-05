from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import User,Record
from django.db.models import Q
def home(request):
    return render(request,"Login.html")


def logoutuser(request):
    logout(request)
    return render(request,"Login.html")



def userreports(request):
    user=User.objects.get(username=request.user)
    print(request.user)
    records=Record.objects.filter(patientname=user)
    print(records)
    context={"reports":records}
    return render(request,"f2.html",context)


def managementlogin(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        try:
            user=User.objects.get(username=username)
        except:
            return render(request,'Login.html',{"error":"User Does't exisit "})
        if user.is_staff==True:
            passw=user.password
            user=authenticate(username=username,password=password)
            if user is not None or passw==password:
                login(request,user,backend='django.contrib.auth.backends.ModelBackend')
                return redirect("management-control")
            else:
                return render(request,'Login.html',{"error":"Wrong credentials"})
        else:
                return render(request,'Login.html',{"error":"Not allowed"})
    return render(request,'Login.html')

def patientlogin(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        try:
            user=User.objects.get(username=username)
        except:
            return render(request,'Login.html',{"error":"User Does't exisit "})
        if user.is_paitent==True or user.is_staff==True:
            passw=user.password
            user=authenticate(username=username,password=password)
            if user is not None or passw==password:
                login(request,user,backend='django.contrib.auth.backends.ModelBackend')
                return redirect('userreports')
            else:
                return render(request,'Login.html',{"error":"Wrong credentials"})
        else:
                return render(request,'Login.html',{"error":"Not allowed"})
    return render(request,'Login.html')


def management(request):
    return render(request,"Management.html")



def createpatient(request):
    if request.method=="POST":
        try:
            username=request.POST.get("username")
            password=request.POST.get("password")
            gender=request.POST.get("gender")
            mobile=request.POST.get("mobileno")
            email=request.POST.get("email")
            dob=request.POST.get("date")
            blood=request.POST.get("blood")
            address=request.POST.get("address")
            user=User.objects.create(username=username,gender=gender,email=email,Mobile=mobile,dob=dob,bloodgroup=blood,address=address,is_paitent=True)
            user.set_password(password)
            user.save()
            return redirect('management-control')
        except:
            return render(request,"createpatient.html",{"error":"Try to change username!!"})
    return render(request,"createpatient.html")


def createManager(request):
    if request.method=="POST":

        try:
            username=request.POST.get("username")
            password=request.POST.get("password")
            gender=request.POST.get("gender")
            mobile=request.POST.get("mobileno")
            email=request.POST.get("email")
            dob=request.POST.get("date")
            blood=request.POST.get("blood")
            address=request.POST.get("address")
            user=User.objects.create(username=username,gender=gender,email=email,Mobile=mobile,dob=dob,bloodgroup=blood,address=address,is_staff=True)
            user.set_password(password)
            user.save()
            return redirect('management-control')
        except:
            return render(request,"createmanage.html",{"error":"Try to change username!!"})
    return render(request,"createmanage.html")


def createreport(request):
    if request.method=="POST":
        username=request.POST.get("username")
        gender=request.POST.get("gender")
        dob=request.POST.get("date")
        blood=request.POST.get("blood")
        dname=request.POST.get("dname")
        prescription=request.POST.get("prescription")
        try:
            user=User.objects.get(username=username)
        except:
            return render(request,"createreport.html",{'error':"Check your username"})
        if user is not None:
            Record.objects.create(patientname=user,gender=gender,dob=dob,bloodgroup=blood,prescription=prescription,Doctorname=dname)
            return redirect('management-control')
        
    return render(request,"createreport.html")

def allreports(request):
    report=Record.objects.filter()
    search=request.GET.get('q')  if request.GET.get('q') != None else ""
    context={"reports":report}
    reports=report.filter(Q(patientname__username__icontains=search)|
                                    Q(Doctorname__icontains=search)|
                                    Q(Record_id__icontains=search))
    context={"reports":reports}
    return render(request,"allreports.html",context)


def checkmobile(request):
    if request.method=="POST":
        mobileno=request.POST.get("mobileno")
        users=User.objects.filter(Mobile=mobileno)
        return render(request,"createreport.html",{"users":users})
    return render(request,"createreport.html")
