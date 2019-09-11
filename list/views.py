# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import TodoList
from .serializers import TodoListSerializers
from django.views.decorators.csrf import csrf_exempt



def index(request):
    get_data = TodoList.objects.all()
    serialized = TodoListSerializers(get_data, many=True)
    return JsonResponse(serialized.data, safe=False)

@csrf_exempt
def create(request):
    TodoList.objects.create(
        name = request.POST.get('name'),
        start_date = request.POST.get('start_date'),
        end_date = request.POST.get('end_date'),
    )
    return HttpResponse('ok')

@csrf_exempt
def update(request, this_id):
    try:
        change = TodoList.objects.get(id=this_id)
        change.name = change.name if request.POST.get('name') is None else request.POST.get('name')
        change.start_date = change.start_date if request.POST.get('start_date') is None else request.POST.get('start_date')
        change.end_date = change.end_date if request.POST.get('end_date') is None else request.POST.get('end_date')
        change.save()
        return HttpResponse(change)
    except:
        return HttpResponse('data tidak ditemukan')

@csrf_exempt    
def delete(request,this_id):
    try:
        erase = TodoList.objects.get(id=this_id)
        erase.delete()
        return HttpResponse('ok')
    except:
        return HttpResponse('data tidak ditemukan')