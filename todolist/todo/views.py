from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from .models import Task


# Create your views here.
def task_list(request):
  task = Task.objects.all().order_by('-created_at')
  return render(request,'todo/task_list.html',{'tasks':task})


def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()

        if title:
            Task.objects.create(
                title=title,
                description=description
            )
            return redirect('todo:task_list')

        error = "Title cannot be empty."
        return render(request,'todo/task_form.html',{'error': error})

    return render(request, 'todo/task_form.html')

def task_update(request,pk):
  task = get_object_or_404(Task, pk = pk)
  if request.method == 'POST':
    title = request.POST.get('title','').strip()
    description = request.POST.get('description','').strip()
    complated = request.POST.get('complated') == 'on'
    if title:
      task.title = title
      task.description = description
      task.complated = complated
      task.save()
      return redirect(reverse('todo:task_list'))
    return render(request,'todo/task_form.html',{'task':task,'error':"Title connot be empty."})
  return render(request,'todo/task_form.html',{'task':task})

def task_delete(request, pk):
  task = get_object_or_404(Task, pk=pk)
  if request.method == 'POST':
    task.delete()
    return redirect(reverse('todo:task_list'))
  return render(request,'todo/task_confirm_delete.html',{'task':task})

def task_toggle_complate(request, pk):
  task=get_object_or_404(Task, pk=pk)
  if request.method == 'POST':
    task.complated = not task.complated
    task.save()

  return redirect('todo:task_list')