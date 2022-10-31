from django.shortcuts import render
from .models import DataTerminals
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F, When, Case, Q

# Create your views here.

def index(request):
    data_list = DataTerminals.objects.all().values()
    return JsonResponse(data={'Inventory': list(data_list)}, status=status.HTTP_200_OK)

def get_switch_status(request):
    if request.method == 'GET':
        queryset = DataTerminals.objects.all().values()
        if queryset is not None:
            # Update switch status to 0 if all P1-P5 is 0
            val1 = queryset.filter(terminal_1__exact=0).filter(terminal_2__exact=0).filter(terminal_3__exact=0).filter(terminal_4__exact=0).filter(terminal_5__exact=0).update(switch_status=0)
            # Update switch status to 1 
            # if val1 is not None:
            #     val2 = queryset.update(switch_status=1)
            # new_val = Case(
            #     Q(terminal_1__exact=0) & Q(terminal_2__exact=0) & Q(terminal_3__exact=0) & Q(terminal_4__exact=0) & Q(terminal_5__exact=0),
            #     then=Value(DataTerminals.0),
            #     default=Value(DataTerminals.1)
            # )
            # print('value is',queryset)
            # queryset.objects.update(switch_status=new_val)
            # for i in queryset:
            #     queryset.switch_status=0
            #     queryset.save()
                # if queryset == 0:
                #     queryset.switch_status = 0
                # else:
                #     queryset.switch_status = 1
            # queryset.save()
            return HttpResponse('<h1>Switch status updated!</h1>')

                    

