from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DeleteView, ListView
from django.urls import reverse_lazy
from app.models import Todo
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

class TodoListView(ListView):
    context_object_name = 'todos'
    model = Todo
    
class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("app:index")

def addTodo(request):
    obj = Todo()
    obj.task = request.POST['task']
    obj.save()
    return redirect('app:index')

def make_completed(request, pk):
    obj = Todo.objects.get(id = pk)
    obj.completed = True
    obj.save()
    return redirect('app:index')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("app:index")
        else:
            form = UserCreationForm()
    return render(request, 'registration/register.html', {'form':form})