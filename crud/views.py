from django.shortcuts import render,redirect
from .models import Employe
from django.contrib import messages
# Create your views here.

def index(request):
    data=Employe.objects.all()
    print(data)
    context={"data":data}
    return render(request,"index.html",context)


def insertData(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        desig=request.POST.get('desig')
        age=request.POST.get('age')
        number=request.POST.get('number')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        # print(name,email,age,gender)
        query=Employe(name=name,email=email,desig=desig,age=age,number=number,gender=gender,address=address)
        query.save()
        messages.info(request,"Data Inserted Successfully")
        return redirect("/")

    return render(request,"index.html")


def updateData(request,id):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        desig=request.POST['desig']
        age=request.POST['age']
        number=request.POST['number']
        gender=request.POST['gender']
        address=request.POST['address']

        edit=Employe.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.desig=desig
        edit.gender=gender
        edit.number=number
        edit.age=age
        edit.address=address
        edit.save()
        messages.warning(request,"Data Updated Successfully")
        return redirect("/")

    d=Employe.objects.get(id=id) 
    context={"d":d}
    return render(request,"edit.html",context)

def deleteData(request,id):
    d=Employe.objects.get(id=id) 
    d.delete()
    messages.error(request,"Data deleted Successfully")
    return redirect("/")