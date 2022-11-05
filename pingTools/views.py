from django.shortcuts import render
from .models import DataTerminals
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F, When, Case, Q, CharField, Value
from datetime import datetime
# import datetime
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib.dates as md
import matplotlib
import dateutil
import seaborn as sns
matplotlib.use('SVG')

# Handle date time conversions between pandas and matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

plt.rcParams["figure.autolayout"] = True

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
    # To convert unix timestamp to datetime and update to DB
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

    s1_info = df.loc[(df['switch'] == 'S1')]
    s2_info = df.loc[(df['switch'] == 'S2')]
    s3_info = df.loc[(df['switch'] == 'S3')]
    date_list_s1 = s1_info['date'].dt.strftime("%Y-%m-%d %H:%M:%S").values.tolist()
    date_list_s2 = s2_info['date'].dt.strftime("%Y-%m-%d %H:%M:%S").values.tolist()
    date_list_s3 = s3_info['date'].dt.strftime("%Y-%m-%d %H:%M:%S").values.tolist()

    switch_status_s1 = s1_info['switch_status'].values.tolist()
    switch_status_s2 = s2_info['switch_status'].values.tolist()
    switch_status_s3 = s3_info['switch_status'].values.tolist()
    df_s1 = pd.DataFrame({'date_list_s1': date_list_s1, 'switch_status': switch_status_s1})[0:361]
    df_s2 = pd.DataFrame({'date_list_s2': date_list_s2, 'switch_status': switch_status_s2})[0:361]
    df_s3 = pd.DataFrame({'date_list_s3': date_list_s3, 'switch_status': switch_status_s3})[0:361]
    # Create figure and plot space
    fig, ax = plt.subplots(figsize=(80, 10), dpi=80)
    # plt.xticks([0, 360])
    plt.yticks([0, 1])
    plt.xticks(rotation = 90)
    plt.locator_params(axis='x', nbins=361)
    fig.subplots_adjust(bottom=0.5)

    # Add x-axis and y-axis
    ax.plot(df_s1['date_list_s1'],df_s1['switch_status'],
            color='purple')

    # Set title and labels for axes
    ax.set(xlabel="Time",
        ylabel="Switch Status",
        title="Switch SW-1 Ping Availability 28-11-2019 (12 am-12 pm)")
    plt.savefig('Switch SW-1 Ping Availability 28-11-2019 (12 am-12 pm).png')

    fig2, ax2 = plt.subplots(figsize=(80, 10), dpi=80)
    # plt.xticks([0, 360])
    plt.yticks([0, 1])
    plt.xticks(rotation = 90)
    plt.locator_params(axis='x', nbins=361)
    fig2.subplots_adjust(bottom=0.5)

    # Add x-axis and y-axis - 2nd plot
    ax2.plot(df_s2['date_list_s2'],df_s2['switch_status'],
            color='red')

    # Set title and labels for axes
    ax2.set(xlabel="Time",
        ylabel="Switch Status",
        title="Switch SW-2 Ping Availability 28-11-2019 (12 am-12 pm)")
    plt.savefig('Switch SW-2 Ping Availability 28-11-2019 (12 am-12 pm).png')

    fig3, ax3 = plt.subplots(figsize=(80, 10), dpi=80)
    # plt.xticks([0, 360])
    plt.yticks([0, 1])
    plt.xticks(rotation = 90)
    plt.locator_params(axis='x', nbins=361)
    fig3.subplots_adjust(bottom=0.5)

    # Add x-axis and y-axis - 2nd plot
    ax3.plot(df_s3['date_list_s3'],df_s3['switch_status'],
            color='blue')

    # Set title and labels for axes
    ax3.set(xlabel="Time",
        ylabel="Switch Status",
        title="Switch SW-3 Ping Availability 28-11-2019 (12 am-12 pm)")
    plt.savefig('Switch SW-3 Ping Availability 28-11-2019 (12 am-12 pm).png')
    return HttpResponse('<h1>Chart created!</h1>')
                    
def create_alert_report(request):
    if request.method == 'GET':
        queryset = DataTerminals.objects.all().values('switch','switch_status','date')
        if queryset is not None:
            alert_report = queryset.filter(switch_status=0).annotate(alert_type=Value('Ping Lost',output_field=CharField()))
            return render(request, 'ping_tool/index.html', {'alert_report': alert_report})

