from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from todo.models import *
# from django.http import HttpResponse

@login_required(login_url='/admin/login/')
def home(request):
    todos = Todo.objects.filter(
        is_active=True,
        user = request.user
        )
    
    context = dict(
        todos=todos
    )
    return render(request,'todo/todo_list.html',context)
@login_required(login_url='/admin/login/')
def category_detail(request,category_slug):
    category = get_object_or_404(Category, slug = category_slug)
    todos = Todo.objects.filter(
        is_active=True,
        category=category,
        user = request.user
        )
    context=dict(
        todos=todos,
        category = category,
    )
    return render(request,'todo/todo_list.html',context)

@login_required(login_url='/admin/login/')
def detail(request,id,category_slug):
    todo = get_object_or_404(Todo,category__slug = category_slug,pk=id,user=request.user)
    context = dict(
        todo = todo,
    )
    return render(request,'todo/todo_detail.html',context)

@login_required(login_url='/admin/login/')
def tag_view(request,tag_slug):
    tag = get_object_or_404(Tag,slug=tag_slug)
    context = dict(
        tag=tag,
        todos=tag.todo_set.filter(user=request.user),
    )
    return render(request,'todo/todo_list.html',context)
