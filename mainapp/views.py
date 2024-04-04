from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from .models import CustomUser,Company, Employee, Job_Post, Course
from django.views import generic

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


    
#use this to restrict a view function  to regestred users
#@login_required
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_jobs = Job_Post.objects.all().count()
    num_courses = Course.objects.all().count()
    num_users_employee = CustomUser.objects.filter(role__exact=2).count()
    num_users = CustomUser.objects.all().count()

    # The 'all()' is implied by default.
    num_company = Company.objects.count()

    #Session uses
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

    # Render the HTML template index.html with the data in the context variable
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
    context_object_name = 'Employee_list'   # your own name for the list as a template variable
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
    context_object_name = 'Course_list'   # your own name for the list as a template variable
    paginate_by = 10

class CourseDetailView(generic.DetailView):
    model = Course
    context_object_name = 'Course'

class CompanyDetailView(generic.DetailView):
    model = Company
    context_object_name = 'Company'
   






'''
from django.contrib.auth.mixins import LoginRequiredMixin

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return (
            BookInstance.objects.filter(borrower=self.request.user)
            .filter(status__exact='o')
            .order_by('due_back')
        )
'''