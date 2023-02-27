from django.shortcuts import render
from django.http import JsonResponse
import asyncio

# Create your views here.


async  def login(request):
    response_data = {'status': '5arya', 'message': 'Invalid credentials'}

    print('test')
    return JsonResponse(response_data,safe=False)