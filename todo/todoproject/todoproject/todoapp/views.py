from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from .forms import TodoForm
from . models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
# Create your views here.


class Tasklistview(ListView):
    model = Task
    template_name= 'home.html'
    context_object_name='task1'

class TaskDetailView(DetailView):
    model = Task
    template_name= 'details.html'
    context_object_name='task'

class TaskUpdateView(UpdateView):
    model = Task
    template_name ='update.html'
    context_object_name ='task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('details',kwargs={'pk':self.object.id})

def home(request):
    task = Task.objects.all()
    if request.method=="POST":
        name=request.POST.get('task')
        priority=request.POST.get('priority')
        date = request.POST.get('date')
        todo=Task(name=name,priority=priority,date=date)
        todo.save()

    return render(request,"home.html",{'task':task})

#def details(request):
  #  task=Task.objects.all()
   # return render(request,"details.html",{'task':task})


def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,"delete.html")

def update(request,id):
    task = Task.objects.get(id=id)
    f=TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})