from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required  # Ensures only logged-in users can access this page
def dashboard(request):
    return render(request, 'secure/dashboard.html')