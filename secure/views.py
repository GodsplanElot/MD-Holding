from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import UserSignupForm
from django.contrib import messages
from .models import Balance

# Create your views here.


@login_required
def dashboard(request):
    balance = Balance.objects.get(user=request.user)
    return render(request, 'secure/dashboard.html', {'balance': balance})

@login_required  # Ensures user must be logged in to access
def dashboard_view(request):
    user = request.user
    # Fetch any additional data you want to display on the dashboard
    context = {
        'user': user,
        # Include additional context if necessary
    }
    return render(request, 'secure/dashboard.html', context)


class CustomLoginView(LoginView):
    template_name = 'secure/login.html'  # Path to your login template
    redirect_authenticated_user = True
    next_page = reverse_lazy('dashboard')  # Redirect to the dashboard


def signup_view(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfuly please log in  ')
            # You can log the user in after signup if you wish:
            # login(request, user)
            return redirect('account_login')  # Redirect to login after successful signup
        else:
            messages.error(request, 'There was an error with your form submission. Please try again')
    else:
        form = UserSignupForm()

    return render(request, 'secure/signup.html', {'form': form})


@login_required
def dashboard(request):
    # Fetch the logged-in user's balance
    balance = None
    try:
        balance = Balance.objects.get(user=request.user)
    except Balance.DoesNotExist:
        pass  # If no balance is found, you can handle it as needed
    
    context = {
        'balance': balance,
    }
    return render(request, 'secure/dashboard.html', context)