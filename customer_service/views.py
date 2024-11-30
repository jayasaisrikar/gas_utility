from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, ServiceRequestForm
from .models import ServiceRequest

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            messages.success(request, 'Service request submitted successfully.')
            return redirect('track_request')
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_request.html', {'form': form})

@login_required
def track_request(request):
    user_requests = ServiceRequest.objects.filter(customer=request.user).order_by('-created_at')
    return render(request, 'track_request.html', {'user_requests': user_requests})


from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            return self.post(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)
