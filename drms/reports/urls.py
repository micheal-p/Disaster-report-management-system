from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL
    path('report/', views.report, name='report'),
    path('report/list/', views.report_list, name='report_list'),  # URL for the report list view
    path('emergency-hotlines/', views.emergency_hotlines, name='emergency'),
]
