from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy


# flash messages display alert to template that disapppear on the next request
def register(request):
    # if we get a post request it creates a form with that post data
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('login')
    # otherwise it will create a blank form
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


class EditProfile(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'editProfile.html'
    success_url = reverse_lazy('site-home')

    # pass in current user
    def get_object(self):
        return self.request.user


@login_required
def account(request):
    return render(request, 'account.html')
