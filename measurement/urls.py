from django.urls import path
from .views import SensorListCreateView, SensorUpdateView, MeasurementView

urlpatterns = [
    path('sensors', SensorListCreateView.as_view()),
    path('sensors/<pk>/', SensorUpdateView.as_view()),
    path('measurements/', MeasurementView.as_view()),

]
