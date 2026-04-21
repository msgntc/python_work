from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """regaster new user."""
    if request.method != 'POST':
        #display blank registration form.
        form = UserCreationForm()
    else:
        # prosses compleated form
        form = UserCreationForm(data=request.POST)

        if form.is_valid(): 
            new_user = form.save()
            # log in the user and then dirext them to the home page
            login(request, new_user)
            return redirect('learning_logs:index')
    # desplay a blank or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)

