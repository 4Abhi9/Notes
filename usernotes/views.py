from django.shortcuts import render, HttpResponseRedirect
from .models import notes_create
from .forms import NewNote, RegisterNewUserForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.views.generic import View
# Create your views here.

class note_page(View):
    def get(self,request):
        newnote=NewNote
        notes=notes_create.objects.filter(username=self.request.user)
        return render(request,'index.html', {'notes':notes,'newnote':newnote})

    def post(self,request):
        newnote=NewNote(request.POST)
        if newnote.is_valid():
            new_note=newnote.save(commit=False)
            new_note.save()
            return HttpResponseRedirect('/')
        else:
            newnote=NewNote()
        return render(request,'index.html', {'newnote':newnote})

class SignIn_page(View):
    def get(self,request):
        loginform=LoginForm()
        signupform=RegisterNewUserForm()
        return render(request, 'SignIn.html', {'loginform':loginform,'signupform':signupform})

    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            self.errors="UserName or Password is wrong"

        signupform=RegisterNewUserForm(request.POST)
        if signupform.is_valid():
            self.errors=""
            signup_form=signupform.save(commit=False)
            signup_form.save()
            return HttpResponseRedirect('/')
        else:
            signupform=RegisterNewUserForm()

        loginform=LoginForm()
        signupform=RegisterNewUserForm()
        return render(request,'SignIn.html',{'loginform':loginform,'signupform':signupform,'errors':errors})

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
