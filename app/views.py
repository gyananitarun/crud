from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title:
            Task.objects.create(title=title, description=description)
        return redirect('index')

    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'index.html', context)

def update_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.completed = not task.completed
    task.save()
    return redirect('index')

def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect('index')
