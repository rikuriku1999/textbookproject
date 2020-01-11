from django.shortcuts import render ,redirect
from .models import Textbookmodel ,Commentmodel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def listfunc(request):
    object_list = Textbookmodel.objects.all()
    return render(request, 'list.html',{'object_list':object_list})


class Create(CreateView):
    template_name='create.html'
    model=Textbookmodel
    fields = ('title','content','author','images')
    success_url = reverse_lazy('list')

def detailfunc(request,pk):
    object_list = Textbookmodel.objects.get(pk=pk)
    object_list2 = Commentmodel.objects.all()
    return render(request, 'detail.html',{'object_list':object_list},{'object_list2':object_list2})

def mypagefunc(request):
    object_list = Textbookmodel.objects.all()
    return render(request,)
    
def loginfunc(request):
    if request.method=='POST':
        email2 = request.POST['email']
        password2 = request.POST['password']
        user = authenticate(request, email=email2, password=password2)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('signup')
    return render(request, 'login.html', {'some':100})


def signupfunc(request):
    if request.method =='POST':
        username2 = request.POST['username']
        email2 = request.POST['email']
        password2 = request.POST['password']
        try:
            User.objects.get(email=email2)
            return render(request, 'signup.html', {'error':'このユーザーは登録されています'})

        except :
            user = User.objects.create_user(username2,email2 , password2)
            return render(request, 'login.html', {'some':100})
    return render(request, 'signup.html', {'some':100})