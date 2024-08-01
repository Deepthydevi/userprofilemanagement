from django.contrib.auth import models
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import userprofile
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def CreateProfile(request):

    if request.method=='POST':

        fullname=request.POST.get('fullname')
        gender = request.POST.get('gender')
        dob = request.POST.get('DOB')
        address = request.POST.get('address')
        email = request.POST.get('email')
        mobilenumber = request.POST.get('mobilenumber')
        education = request.POST.get('education')
        skills = request.POST.get('skills')

        users=userprofile(fullname=fullname,gender=gender,DOB=dob,address=address,email=email,mobilenumber=mobilenumber,education=education,skills=skills)
        users.save()


    return render(request,'createprofile.html')

def listdetails(request):
    values=userprofile.objects.all()

    return render(request, 'viewprofile.html', {'values': values})

def editdetails(request, p_id):
    p=userprofile.objects.get(id=p_id)
    if request.method=='POST':
        fullname = request.POST.get('fullname')
        gender = request.POST.get('gender')
        DOB = request.POST.get('DOB')
        address = request.POST.get('address')
        email = request.POST.get('email')
        mobilenumber = request.POST.get('mobilenumber')
        education = request.POST.get('education')
        skills = request.POST.get('skills')

        p.fullname = fullname
        p.gender = gender
        p.DOB = DOB
        p.address = address
        p.email = email
        p.mobilenumber = mobilenumber
        p.education = education
        p.skills = skills
        p.save()
        return redirect('details')
    return render(request, 'editprofile.html', {'p':p})

def deletedetails(request,p_id):
    p = userprofile.objects.get(id=p_id)
    if request.method=='POST':

        p.delete()

        return redirect('details')
    return render(request, 'deleteprofile.html', {'p': p})
