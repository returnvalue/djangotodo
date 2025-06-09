from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from django.contrib import messages


def home(request):
    form = TodoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Task has been added!')
        return redirect('home')
    todos = Todo.objects.all()
    return render(request, 'todoapp/home.html', {'todos': todos})


def delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    messages.success(request, 'Task has been Deleted!')
    return redirect('home')

def _set_completed(todo_id, value):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = value
    todo.save()


def mark_complete(request, todo_id):
    _set_completed(todo_id, True)
    return redirect('home')


def mark_incomplete(request, todo_id):
    _set_completed(todo_id, False)
    return redirect('home')


def edit(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    form = TodoForm(request.POST or None, instance=todo)

    if form.is_valid():
        form.save()
        messages.success(request, 'Task has been edited!')
        return redirect('home')
    return render(request, 'todoapp/edit.html', {'todo': todo})
