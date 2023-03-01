from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SignUpForm


# Create your views here.

def frontpage(request):
    return render(request, 'core/frontpage.html')


def signup(request):
    # handle POST request
    if request.method == 'POST':
        # create instance of signup form
        form = SignUpForm(request.POST)

        # check if data in form is valid
        if form.is_valid():
            # save form and commit to db creating new user
            form.save()

            # login new user
            login(request, user)

            # return user to front page
            return redirect('frontpage')
    
    # handle GET request
    else:
        # create empty instance of signup form
        form = SignUpForm()

    context = {
        'form': form,
    }
    return render(request, 'core/signup.html', context)    
