from django.shortcuts import render, redirect
from .models import Menu, Employee, Quote
from django.contrib.auth import authenticate, login
from .forms import MenuForm, EmployeeForm, QuoteForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth import logout


# Create your views here.
def admin_login(request):
    if request.user.is_authenticated:
        # If user is already logged in, redirect to home page or any other appropriate page
        return redirect('users:nicole')  # Change 'home' to the name of your home page URL pattern

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page
                return redirect('users:nicole')
            else:
                # Handle invalid login
                return render(request, 'users/login.html', {'form': form, 'error_message': 'Invalid username or password.'})
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})




def logo(request):
    return render(request, 'users/logo.html')

def show_homepage(request):
    return render(request, 'users/index.html')


def menu(request):
    beverages = Menu.objects.filter(category='beverages').order_by('item')
    meals = Menu.objects.filter(category='meals').order_by('item')
    snacks = Menu.objects.filter(category='snacks').order_by('item')
    menu_items = Menu.objects.all()
    
    return render(request, 'users/menu.html', {'beverages': beverages, 'meals': meals, 'snacks': snacks,'menu_items':menu_items})

def delete_menu_item(request, item_id):
    if request.method == 'POST':
        try:
            # Retrieve the Menu item
            menu_item = Menu.objects.get(pk=item_id)
        except Menu.DoesNotExist:
            # Handle the case where the menu item doesn't exist
            raise Http404("Menu item does not exist")

        # Delete the item
        menu_item.delete()
        # Redirect to a success page or the menu page
        return redirect('users:menu') 
    else:
        return redirect('users:menu')  # Redirect to the menu page in case of other HTTP methods

def delete_confirmation(request, item_id):
    menu_item = get_object_or_404(Menu, id=item_id)
    return render(request, 'users/delete_confirmation.html', {'menu_item':menu_item})

def logout_view(request):
    logout(request)
    # Redirect to the desired page after logout, for example, the home page
    return redirect('users:show_homepage') 

def about(request):
    return render(request,'users/about.html')

def contact(request):
    return render(request,'users/contact.html')

def employee(request):
    try:
        # Retrieve the last entry from the Employee model
        employee = Employee.objects.latest('id')  # Assuming 'id' is the field representing entry order
    except Employee.DoesNotExist:
        employee = None  # Handle the case where no employee exists
        
    try:
        # Retrieve the last entry from the Employee model
        quote = Quote.objects.latest('id')  # Assuming 'id' is the field representing entry order
    except Quote.DoesNotExist:
        employee = None  # Handle the case where no employee exists
    
    return render(request, 'users/employee.html', {'employee': employee,'quote':quote})





def franchise(request):
    return render(request,'users/franchise.html')

@login_required
def nicole(request):
    if request.method == 'POST':
        menu_form = MenuForm(request.POST, request.FILES)
        employee_form = EmployeeForm(request.POST, request.FILES)
        quote_form = QuoteForm(request.POST, request.FILES)
        if menu_form.is_valid():
            menu_form.save()
            return redirect('users:menu')
        if employee_form.is_valid():
            employee_form.save()
            return redirect('users:employee')
        if quote_form.is_valid():
            quote_form.save()
            # Handle successful quote form submission
            return redirect('users:employee')
    else:
        menu_form = MenuForm()
        employee_form = EmployeeForm()
        quote_form = QuoteForm()
    return render(request, 'users/nicole.html', {'menu_form': menu_form, 'employee_form': employee_form, 'quote_form': quote_form})
