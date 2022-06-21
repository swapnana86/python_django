from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from .models import Task

from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView,DeleteView


class TasklistviewGen(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'detail_task_key'


class TaskdetailviewGen(DetailView):
    model = Task
    template_name = 'showdetails.html'
    context_object_name = 'detailtask'


class TaskupdateviewGen(UpdateView):
    model = Task
    template_name = 'updategen.html'
    context_object_name = 'updatetask'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('cbgvdetail', kwargs={'pk': self.object.id})#first parameter name of url of details

class TaskdeleteviewGen(DeleteView):
         model = Task
         template_name = 'delete.html'
         success_url = reverse_lazy('cbgvhome')#name of url cbgvhome


def add(request):
    details_task_var = Task.objects.all()  # details show in same page
    if request.method == 'POST':
        taskname = request.POST.get('taskname')
        taskpriority = request.POST.get('priority')
        taskdate = request.POST.get('date')
        task1 = Task(name=taskname, priority=taskpriority, date=taskdate)
        task1.save()
    return render(request, 'home.html', {'detail_task_key': details_task_var})


"""def details(request):
    details_task_var = Task.objects.all()
    return render(request, 'showdetails.html', {'detail_task_key': details_task_var})"""


def update(request, taskid):
    task1_var = Task.objects.get(id=taskid)
    form_var = TodoForm(request.POST or None, instance=task1_var)
    if form_var.is_valid():
        form_var.save()
        return redirect('/')
    return render(request, 'edit.html', {'form_key': form_var, 'task1_key': task1_var})


def delete(request, taskid):
    task_var1 = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task_var1.delete()
        return redirect('/')
    return render(request, 'delete.html')
