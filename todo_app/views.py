from django.shortcuts import render, redirect
from django.views import View
from .models import TodoItem
from .forms import TodoForm

class TodoListView(View):
    def get(self, request):
        todos = TodoItem.objects.all().order_by('-created_at')
        form = TodoForm()
        return render(request, 'todo_app/todo_list.html', {'todos': todos, 'form': form})

    def post(self, request):
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('todo_list')

class TodoToggleComplete(View):
    def post(self, request, pk):
        todo = TodoItem.objects.get(pk=pk)
        todo.completed = not todo.completed
        todo.save()
        return redirect('todo_list')