"""
URL configuration for finance_advisor project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('advisor.urls')),
]
