from django.shortcuts import render ,redirect ,get_object_or_404
from .models import Textbookmodel ,Commentmodel ,Usermodel ,Chatroommodel ,Chatmodel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import CreateView ,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from . import forms
from .forms import UserForm

# Create your views here.

def listfunc(request):
    object_list = Textbookmodel.objects.all()
    return render(request, 'list.html',{'object_list':object_list})


class Create(CreateView):
    template_name='create.html'
    model=Textbookmodel
    fields = ('title','content','author','images')
    success_url = reverse_lazy('list')

def chatroomfunc(request,pk):
    object_list = Textbookmodel.objects.get(pk=pk)
    chatroomlist = Chatroommodel(pk=pk)
    
    form = forms.ChatForm(request.POST or None)
    if Chatroommodel.objects.exists():
        pass
    else:
        Chatroommodel.objects.create(
            buyer = request.user,
            target = object_list,
            seller = object_list.author,
        )
    chat_list = Chatroommodel.objects.get(target=object_list)
    chats=Chatmodel.objects.filter(target=chat_list)
    if request.method == "POST":
        if form.is_valid():
            chat = form.save(commit=False)
            if request.user == object_list.author:
                chat.sender = chat_list.seller
                chat.receiver = chat_list.buyer
                chat.target = chat_list
                chat.save()  
            else:
                chat.sender = chat_list.buyer
                chat.receiver = chat_list.seller
                chat.target = chat_list
                chat.save()
        else:
            form = forms.ChatForm()
    return render(request, 'chatroom.html',{
        'chatroomlist':chatroomlist,
        'chats':chats,
        'form':form,
        })

def chatfunc(request,pk):
    form = forms.ChatForm(request.POST or None)
    object_list=Textbookmodel.objects.get(pk=pk)
    chats=Chatmodel.objects.filter(sender=object_list)
    if request.method == "POST":
        if form.is_valid():
            chat = form.save(commit=False)
            chat.sender = object_list.author
            chat.receiver = request.user
            
            chat.save()
        else:
            form = forms.CommentForm()
        
    return render(request, 'chat.html')

def deletefunc(request,pk):
    Textbookmodel.objects.filter(pk=pk).delete()
    return redirect('mypage')

def editdetailfunc(request,pk):
    form = forms.DetailForm(request.POST ,request.FILES)
    detail = Textbookmodel(pk=pk)
    if form.is_valid():
        detail.title = form.cleaned_data['title']
        detail.content = form.cleaned_data['content']
        
        Textbookmodel.objects.filter(pk=pk).update(
            title=detail.title,
            content=detail.content,
            
        )
        return redirect("detail",pk=pk)
    return render(request,'editdetail.html',{
        'form':form,
        'detail':detail,
        })


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
    object_list = Usermodel.objects.all()
    post = Textbookmodel.objects.filter(author__exact=request.user)
    if Textbookmodel.objects.exists():
        return render(request, 'mypage.html',{
            'object_list':object_list,
            'post':post})
    else :
        return render(request, 'mypage.html',{
            'object_list':object_list})

def editmypagefunc(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        profile = Usermodel()
        profile.gender = form.cleaned_data['gender']
        profile.intro = form.cleaned_data['intro']
        profile.college = form.cleaned_data['college']

        if Usermodel.objects.exists():
            Usermodel.objects.update(
                gender=profile.gender,
                college=profile.college,
                intro=profile.intro,
            )
        else:
            Usermodel.objects.create(
                gender=profile.gender,
                college=profile.college,
                intro=profile.intro,
                user=request.user
            )
        return redirect('mypage')

    return render(request, 'editmypage.html', {'form':form})
        

class Editmypage(UpdateView):
    template_name='editmypage.html'
    model=Usermodel
    fields = ('intro','college','gender','user')
    success_url = reverse_lazy('mypage')

def profilefunc(request):
    object_list = Usermodel.objects.all()
    
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
    

