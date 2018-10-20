from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import UserRegistrationForm


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} created!')

            return redirect('blog_home')

    else:
        form = UserRegistrationForm()

    return render(request, 'users/registration.html', {'form': form})
