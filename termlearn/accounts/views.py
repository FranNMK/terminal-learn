from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm



# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # save institution to profile
            institution = form.cleaned_data.get('institution')
            user.profile.institution = institution
            user.profile.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

