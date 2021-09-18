from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.http import HttpResponse
# Create your views here.


# this func will add new and show existing items
def add_show(request):
    if request.method =='POST':
        print("hello")
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})
    

#this function will update/edit
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(id=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(id=id)
        fm = StudentRegistration(instance=pi)    

    return render(request, 'enroll/updatestudent.html',{'form': fm})

#this func wil delete the data
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(id=id)
        pi.delete()
        return HttpResponseRedirect('/')