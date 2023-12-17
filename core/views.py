from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .models import Product

def home(request):
    product = Product.objects.all()
    context={
        'product':product,
    }
    return render(request,'home.html',context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
