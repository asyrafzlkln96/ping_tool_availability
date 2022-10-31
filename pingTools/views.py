from django.shortcuts import render
from .models import DataTerminals
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F, When, Case, Q

# Create your views here.

def index(request):
    data_list = DataTerminals.objects.all().values()
    return JsonResponse(data={'Ping_Statuses': list(data_list)}, status=status.HTTP_200_OK)

def get_switch_status(request):
    if request.method == 'GET':
        queryset = DataTerminals.objects.all().values()
        if queryset is not None:
            # Update switch status to 0 if all P1-P5 is 0
            val1 = queryset.filter(terminal_1__exact=0).filter(terminal_2__exact=0).filter(terminal_3__exact=0).filter(terminal_4__exact=0).filter(terminal_5__exact=0).update(switch_status=0)
            # Update switch status to 1 for other records
            val2 = queryset.filter(Q(terminal_1=1) | Q(terminal_2=1) | Q(terminal_3=1) | Q(terminal_4=1) | Q(terminal_5=1)).update(switch_status=1)
            return HttpResponse('<h1>Switch status updated!</h1>')
