from django.contrib import admin
from django.urls import path
from core.views import CareerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('careers/', CareerView.as_view(), name='career-list'),
]
