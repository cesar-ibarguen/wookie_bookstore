from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account have been created! You are able to Log IN!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'authors/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'authors/profile.html')

