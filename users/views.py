from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from .forms import UserRegisterForm, EditProfileForm, PasswordChangingForm, ProfilePageForm, AddCommentForm
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
from newsite.models import UserProfile, Comment


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


class CreateProfilePage(CreateView):
    model = UserProfile
    form_class = ProfilePageForm
    template_name = "create_user_profile_page.html"
    # Making the user ID available to profile
    # when we save form it will save the user
    # credit to -
    # https://stackoverflow.com/questions/68359593/how-to-write-form-valid-method-in-django-correctly
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddComment(CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('site-home')
    # Making the user ID available to profile
    # when we save form it will save the user
    # credit to -
    # https://stackoverflow.com/questions/68359593/how-to-write-form-valid-method-in-django-correctly

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


class ProfilePage(DetailView):
    model = UserProfile
    template_name = 'userProfile.html'

    def get_context_data(self, *args, **kwargs):
        users = UserProfile.objects.all()
        context = super(ProfilePage, self).get_context_data(*args, **kwargs)

        profile_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])

        context["profile_user"] = profile_user
        return context


class EditProfilePage(generic.UpdateView):
    model = UserProfile
    template_name = 'edit_profile_page.html'
    fields = ['bio', 'profile_picture', 'site_url', 'twitter_url', 'fb_url', 'github_url']
    success_url = reverse_lazy('site-home')


class EditProfile(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'editProfile.html'
    success_url = reverse_lazy('site-home')

    # pass in current user
    def get_object(self):
        return self.request.user


class EditPassword(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')


def PasswordSuccess(request):
    return render(request, 'password_success.html', {})


@login_required
def account(request):
    return render(request, 'account.html')
