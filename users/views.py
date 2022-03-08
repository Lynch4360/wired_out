from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# flash messages display alert to template that disapppear on the next request
def register(request):
    # if we get a post request it creates a form with that post data
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('site-home')
    # otherwise it will create a blank form
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
