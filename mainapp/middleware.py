from django.shortcuts import redirect
from django.urls import reverse



class FirstVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        
        exclude = ["/mainapp/accounts/logout/"]       
        
        if request.user.is_authenticated and request.user.is_firstvisit() and (request.path not in exclude):
            if request.user.is_employee():
                if request.path != reverse('employee-first-visit'):
                    return redirect(reverse("employee-first-visit"))
            elif request.user.is_company():
                if request.path != reverse('company-first-visit'):
                    return redirect(reverse("company-first-visit"))
   

        response = self.get_response(request)
        return response
