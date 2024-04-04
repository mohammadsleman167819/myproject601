from django.urls import path
from . import views
from .views import SignUpView
from django.urls import include


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('', views.index, name='index'),
    path('posts/', views.Job_PostListView.as_view(), name='posts'),
    path('post/<int:pk>', views.Job_PostDetailView.as_view(), name='job_post-detail'),
    path('employees',views.EmployeeListView.as_view(),name='employees'),
    path('employee/<int:pk>', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('courses',views.CourseListView.as_view(),name='courses'),
    path('course/<int:pk>', views.CourseDetailView.as_view(), name='course-detail'),
    path('company/<int:pk>', views.CompanyDetailView.as_view(), name='company-detail'),    
    path('accounts/', include('django.contrib.auth.urls')),

]
