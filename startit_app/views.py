from django.shortcuts import render, get_object_or_404, redirect
from .models import Quest, addresesQ, infotxt
from django.contrib.auth import login, authenticate, logout
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

def home_page(request):
    quests = Quest.objects.all().order_by('-created_at')
    unique_ages = Quest.objects.values('age__name').distinct()
    unique_slozhno = Quest.objects.values('slozhno__name').distinct()
    unique_strashno = Quest.objects.values('strashno__name').distinct()
    infotxts = infotxt.objects.all()

    return render(request, "index.html", {
        'quests': quests,
        'unique_ages': unique_ages,
        'unique_slozhno': unique_slozhno,
        'unique_strashno': unique_strashno,
        'infotxts' : infotxts 
    })

def book_page(request, pk):
    quest = get_object_or_404(Quest, pk=pk)
    addresesq = addresesQ.objects.all()
    return render(request, "book-page.html", {
        'quest': quest,
        'addresesq': addresesq,
    })

def quests_by_home_page(request, slug):
    addresesQ = get_object_or_404(addresesQ, slug=slug)
    quests = Quest.objects.filter(addresesQ=addresesQ)
    context = {
        'addresesQ': addresesQ,
        'quests': quests,
    }
    return render(request, "./quests_by_addresesQ.html", context)

def sign_up_page(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login_page')
            
    else:
        form = NewUserForm()

    context = {
        'form': form
    }
    return render(request, "sign_up.html", context)

def login_page(request):
    if request.method == "POST":
            form = AuthenticationForm(request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home_page')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, "login.html", context)

def logout_action(request):
    logout(request)
    return redirect('home_page')

def filtered_quests(request, filter_type=None, filter_value=None):
    quests = Quest.objects.all()

    if filter_type == 'age':
        quests = quests.filter(age__name=filter_value)
    elif filter_type == 'slozhno':
        quests = quests.filter(slozhno__name=filter_value)
    elif filter_type == 'strashno':
        quests = quests.filter(strashno__name=filter_value)
    infotxts = infotxt.objects.all()

    context = {
        'quests': quests,
        'unique_ages': Quest.objects.values('age__name').distinct(),
        'unique_slozhno': Quest.objects.values('slozhno__name').distinct(),
        'unique_strashno': Quest.objects.values('strashno__name').distinct(),
        'picked_filter': filter_value,  
        'filter_type': filter_type,
        'infotxts' : infotxts,
    }

    return render(request, 'filtered_quests.html', context)
