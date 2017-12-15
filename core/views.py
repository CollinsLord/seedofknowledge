from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    return render(request, 'core/landing.html', {})

def register(request):
    pass

class RegisterView(FormView):
    template_name = 'core/signup.html'
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def dashboard(request):
    return render(request, 'core/dashboard.html', {})
