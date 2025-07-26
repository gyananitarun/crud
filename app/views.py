from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils.timezone import now

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


@csrf_exempt
def save_location(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print("Location Data:", data)  # shows up in Azure logs or console

        # You can optionally save this to DB
        # Location.objects.create(latitude=data['lat'], longitude=data['lng'], address=data['address'])

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'invalid request'}, status=400)
