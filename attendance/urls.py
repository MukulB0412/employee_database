from django.urls import path
from . import views

urlpatterns = [
    path('attendance/', views.AttendanceListCreateAPIView.as_view(), name='attendance'),
    path('attendance/<int:pk>/', views.AttendanceRetrieveUpdateDestroyAPIView.as_view(), name='attendance-detail'),
    path('performance/', views.PerformanceListCreateAPIView.as_view(), name='performance'),
    path('performance/<int:pk>/', views.PerformanceRetrieveUpdateDestroyAPIView.as_view(), name='performance-detail'),
]

