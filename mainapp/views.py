from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from .models import CustomUser,Company, Employee, Job_Post, Course
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import EmployeeInfoForm,CompanyInfoForm
from django.http import HttpResponseRedirect
from django.urls import reverse

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"



    
def index(request):
    
    num_jobs = Job_Post.objects.all().count()
    num_courses = Course.objects.all().count()
    num_users_employee = CustomUser.objects.filter(role__exact=2).count()
    num_users = CustomUser.objects.all().count()
    num_company = Company.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1


    context = {
        'num_jobs': num_jobs,
        'num_courses': num_courses,
        'num_users_employee': num_users_employee,
        'num_company': num_company,
        'num_users':num_users,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)


class Job_PostListView(generic.ListView):

    
    model = Job_Post
    context_object_name = 'Job_Post_list'   # your own name for the list as a template variable
    paginate_by = 10
    '''
    def get_queryset(self):
        return Book.objects.filter(title__icontains='war')[:5] #
    '''
    #context_object_name = 'book_list'   # your own name for the list as a template variable
    #queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    #template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location
    '''
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context
    '''

class Job_PostDetailView(generic.DetailView):
    model = Job_Post
    context_object_name = 'Job_Post'


class EmployeeListView(generic.ListView):
    model = Employee
    context_object_name = 'Employee_list'
    paginate_by = 10

class EmployeeDetailView(generic.DetailView):
    model = Employee
    context_object_name = 'Employee'
    def get_context_data(self, **kwargs):
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)
        emp = self.get_object()
        context['Age'] = emp.get_age()
        return context

class CourseListView(generic.ListView):
    model = Course
    context_object_name = 'Course_list'
    paginate_by = 10

class CourseDetailView(generic.DetailView):
    model = Course
    context_object_name = 'Course'

class CompanyDetailView(generic.DetailView):
    model = Company
    context_object_name = 'Company'
   




@login_required
def firstVisitEmployee(request):
    if request.method == 'POST':
        form = EmployeeInfoForm(request.POST)
        if form.is_valid():
            user = request.user
            user.firstvisit = 0
            user.save()
            new_employee = Employee.objects.create(employee_id=user,**form.cleaned_data)
            new_employee.save()
            # Redirect to success page or dashboard after successful creation
            return HttpResponseRedirect(reverse('index'))  
    else:
        form = EmployeeInfoForm()
    return render(request, 'mainapp/create_employee.html', {'form': form})



@login_required
def firstVisitCompany(request):
    if request.method == 'POST':
        form = CompanyInfoForm(request.POST)
        if form.is_valid():
            user = request.user
            user.firstvisit = 0
            user.save()
            new_company = Company.objects.create(company_id=user,**form.cleaned_data)
            new_company.save()
            return HttpResponseRedirect(reverse('index'))  
    else:
        form = CompanyInfoForm()
    return render(request, 'mainapp/create_company.html', {'form': form})