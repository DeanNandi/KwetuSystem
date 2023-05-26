from django.shortcuts import render, redirect, get_object_or_404
from .models import Donors
from .forms import MyForm
from .filters import OrderFilter
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('/')

        context = {'form': form}
        return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')



def index(request):
    donors = Donors.objects.all()

    myFilter = OrderFilter(request.GET, queryset=donors)
    donors = myFilter.qs

    total_donors = donors.count()

    context = {'donors': donors, 'myFilter': myFilter, 'total_donors': total_donors}

    return render(request, 'index.html', context)


def delete_donors(request, pk):
    template = 'index.html'
    Donors.objects.filter(id=pk).delete()

    donors = Donors.objects.all()

    context = {
        'donors': donors,
    }

    return render(request, template, context)


def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = cls(instance=item)

        return render(request, 'edit_item.html', {'form': form})


def edit_donors(request, pk):
    return edit_item(request, pk, Donors, MyForm)


def my_form(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = MyForm()
    return render(request, 'cv-form.html', {'form': form})

