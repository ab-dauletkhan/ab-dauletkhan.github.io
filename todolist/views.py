from django.shortcuts import render
from .forms import UserRegisterForm


def index(request):
    return render(request, 'todolist/index.html')


def register_account(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)

            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'todolist/index.html')

    else:
        user_form = UserRegisterForm()

    return render(request, 'todolist/register.html', {'user_form': user_form})