from django.urls import path
from mainapp import views
from .views import SignUpView
from django.urls import include


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('', views.index, name='index'),
    
    
    path('posts/', views.Job_PostListView.as_view(), name='posts'),
    path('post/<int:pk>', views.Job_PostDetailView.as_view(), name='job_post-detail'),
    path('courses',views.CourseListView.as_view(),name='courses'),
    path('course/<int:pk>', views.CourseDetailView.as_view(), name='course-detail'),
    path('company/<int:pk>', views.CompanyDetailView.as_view(), name='company-detail'),    
    
    path('employee/firstvisit/', views.firstVisitEmployee, name='employee-first-visit'),    
    
    path('company/firstvisit/', views.firstVisitCompany, name='company-first-visit'),    
    path('company/listemployees',views.EmployeeListView.as_view(),name='list-employees'),
    path('company/viewemployee/<int:pk>', views.EmployeeDetailView.as_view(), name='employee-detail'),
    
]
