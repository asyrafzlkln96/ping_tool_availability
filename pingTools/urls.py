from django.urls import path
# from .views import index
from . import views

app_name = 'pingTools'

urlpatterns = [
    path("pingtool", views.index, name="get_all_ping_status"),
    path("update_switch_status", views.get_switch_status, name="update_switch_status")
]