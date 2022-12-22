from django.shortcuts import render
import random


def monday(request):
    todo_list = ['Помыть посуду', 'Сделать домашку', 'Погулять']
    random.shuffle(todo_list)
    return render(request, 'monday.html', {'todo_list': todo_list})
# Create your views here.
