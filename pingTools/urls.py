from django.urls import path
# from .views import index
from . import views

app_name = 'pingTools'

urlpatterns = [
    path("pingtool", views.index, name="get_all_ping_status"),
    path("update_switch_status", views.get_switch_status, name="update_switch_status"),
    path("update_timestamp", views.convert_unix_timestamp_to_datetime, name="timestamp_conversion"),
    path("create_chart", views.create_chart, name="generate_switch_status_chart"),
    path("report", views.create_alert_report, name="create_alert_report")
]
