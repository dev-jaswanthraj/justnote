from typing import Text
from django.http import request
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import (
    note,
    todo
)
from .form import (
    create,
    note_form
)
# Create your views here.
def home(request):
    if str(request.user) != 'AnonymousUser':
        logout(request)
        
    return render(request, 'firstpage.html')

@login_required(login_url='/login')
def home_user(request):
    user_id = User.objects.get(username = request.user)
    top_five = todo.objects.filter(done = False, user_id = user_id).order_by('-id')[:6]
    print('hi')
    context = {
        'top_five':top_five,
    }
    return render(request, 'home.html', context)

def sign_up(request):
    form = create()
    if request.method == 'POST':
        form = create(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "The user is created Succesfully!!!")
            return redirect('/login')
    context = {
        'form':form
    }
    return render(request, 'signup.html', context)

def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['pwd']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            request.session['user_flag'] = True
            return redirect('/home')
        else:
            messages.info(request, "The username or password is incorrect!!")
            return render(request, 'login.html')
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login')
def para(request, id):
    user_id = User.objects.get(id = id)
    lst = note.objects.filter(user_id = user_id).order_by('-id')
    context ={
        'lst':lst
    }
    return render(request, 'paragraph.html',context)

@login_required(login_url='/login')
def create_para(request, id):
    form = note_form()
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        user_id = User.objects.get(id = id)
        Note = note.objects.create(user_id = user_id, title = title, content = content)
        Note.save()
        return redirect('/paragraph/'+str(id))
    context = {
        'form':form,
        'flag':True
    }
    return render(request, 'paragraph/create.html', context)

@login_required(login_url='/login')
def update(request, id):
    Notes = note.objects.get(id = id)
    user_id = Notes.user_id.id
    form = note_form(instance=Notes)
    if request.method == 'POST':
        form = note_form(request.POST, instance=Notes)
        if form.is_valid:
            instance = form.save(commit=False)
            instance.save()
            return redirect('/paragraph/'+str(user_id))

    context = {
        'form':form,
        'post_id':id,
    }
    return render(request, 'paragraph/create.html', context)

@login_required(login_url='/login')
def delete_note(request, id):
    Note = note.objects.get(id = id)
    Note.delete()
    return redirect('/paragraph/'+str(Note.user_id.id)) 

@login_required(login_url='/login')
def check_box(request, id):
    user_id = User.objects.get(id = id)
    not_done_todo_list = todo.objects.filter(user_id = user_id, done = False)
    done_todo_list = todo.objects.filter(user_id = id, done = True)
    if request.method == 'POST':
        content = request.POST['content']
        obj = todo.objects.create(user_id = user_id ,content = content)
        obj.save()
        return redirect('/todo/'+str(id))
    context = {
        'not_done_todo_list':not_done_todo_list,
        'done_todo_list':done_todo_list
    }
    
    return render(request, 'checkbox/todo.html', context)
    

@login_required(login_url='/login')
def todo_done(request, id):
    ins = todo.objects.get(id = id)
    ins.done = True
    ins.save(update_fields = ['done'])
    return redirect('/todo/'+str(ins.user_id.id))

@login_required(login_url='/login')
def todo_del(request, id):
    ins = todo.objects.get(id = id)
    ins.delete()
    return redirect('/todo/'+str(ins.user_id.id))

@login_required(login_url='/login')
def post_view(request, id):
    Notes = note.objects.get(id = id)
    context = {
        'Note':Notes,
        'post_id':id,
    }
    return render(request, 'paragraph/noteview.html', context)

@login_required(login_url='/login')
def search(request):
    title = request.POST.get('item')
    if title == '':
        return render(request, 'home.html')
    user_id = User.objects.get(username = request.user)
    Note = note.objects.filter(title__contains = title, user_id = user_id)
    context = {
        'search_flag':True,
        'Note':Note,
    }
    return render(request, 'home.html', context)

    