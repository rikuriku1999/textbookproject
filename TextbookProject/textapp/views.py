from django.shortcuts import render ,redirect
from .models import Textbookmodel ,Commentmodel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from . import forms

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
    comments = Commentmodel.objects.filter(target=object_list)
    form = forms.CommentForm(request.POST or None)

    if request.method == "POST":
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.target = object_list
            comment.author = request.user
            comment.save()
        else:
            form = forms.CommentForm()

    return render(request, 'detail.html',{
        'object_list':object_list,
        'form':form,
        'comments':comments
        })
            


def mypagefunc(request):
    object_list = Textbookmodel.objects.all()
    return render(request, '')
    
def loginfunc(request):
    if request.method=='POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
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
            User.objects.get(username=username2)
            return render(request, 'signup.html', {'error':'このユーザーは登録されています'})

        except :
            user = User.objects.create_user(username2,email2 , password2)
            return render(request, 'list.html', {'some':100})
    return render(request, 'signup.html', {'some':100})

def goodfunc(request,pk):
    post=Textbookmodel.objects.get(pk=pk)
    post2=request.user.get_username()
    if post2 in post.goodtext:
        return redirect('detail' ,pk=pk)
    else:
        post.good +=1
        post.goodtext=post.goodtext + ' ' + post2
        post.save()
    return redirect('detail' ,pk=pk)
    

