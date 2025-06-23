from django.urls import path
from . import views

urlpatterns = [
    path('departments/', views.DepartmentListCreateAPIView.as_view(), name='departments'),
    path('employees/', views.EmployeeListCreateAPIView.as_view(), name='employees'),
    path('employees/<int:pk>/', views.EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='employee-detail'),
]

