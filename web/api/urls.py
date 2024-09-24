from django.urls import path
from .views import (UserLoginView, UserRegistrationView, CareerListCreateView, CareerDetailView,
                    CourseDetailsView, CourseListCreateView)

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('careers/', CareerListCreateView.as_view(), name='career-list-create'),
    path('careers/<uuid:id>/', CareerDetailView.as_view(), name='career-detail'),
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<uuid:id>/', CourseDetailsView.as_view(), name='course-detail'),
]
