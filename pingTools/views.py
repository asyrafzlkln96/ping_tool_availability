from django.shortcuts import render
from .models import DataTerminals
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F, When, Case, Q, CharField, Value
from datetime import datetime
# import datetime
import pandas as pd
# import datetime as dt
import matplotlib.pyplot as plt


# Create your views here.

def index(request):
    data_list = DataTerminals.objects.all().values()
    return JsonResponse(data={'Ping_Statuses': list(data_list)}, status=status.HTTP_200_OK)

def get_switch_status(request):
    if request.method == 'GET':
        queryset = DataTerminals.objects.all().values()
        if queryset is not None:
            timestamp = queryset.values_list('timestamp', flat=True)
            # Update switch status to 0 if all P1-P5 is 0
            val1 = queryset.filter(terminal_1__exact=0).filter(terminal_2__exact=0).filter(terminal_3__exact=0).filter(terminal_4__exact=0).filter(terminal_5__exact=0).update(switch_status=0)
            # Update switch status to 1 for other records
            val2 = queryset.filter(Q(terminal_1=1) | Q(terminal_2=1) | Q(terminal_3=1) | Q(terminal_4=1) | Q(terminal_5=1)).update(switch_status=1)
            return HttpResponse('<h1>Switch status updated!</h1>')

def convert_unix_timestamp_to_datetime(request):
    # To convert unix timestamp to datetime
    df =  pd.DataFrame(list(DataTerminals.objects.all().values('timestamp')))
    df2 = df.astype('int').astype("datetime64[s]")
    data_dict = df2.to_dict()['timestamp']
    bulk_update_list = []
    for key, value in data_dict.items():
        querys = DataTerminals.objects.get(id=key+1)
        querys.date = value
        bulk_update_list.append(querys)
    DataTerminals.objects.bulk_update(bulk_update_list, ['date'])
    return HttpResponse('<h1>Timestamp updated!</h1>')

def create_chart(request):
    df = pd.DataFrame(list(DataTerminals.objects.all().values('switch','switch_status','date')))
    print('df is:', df)
    return HttpResponse('<h1>Chart created!</h1>')
                    
def create_alert_report(request):
    if request.method == 'GET':
        queryset = DataTerminals.objects.all().values('switch','switch_status','date')
        if queryset is not None:
            alert_report = queryset.filter(switch_status=0).annotate(alert_type=Value('Ping Lost',output_field=CharField()))
            return render(request, 'ping_tool/index.html', {'alert_report': alert_report})

