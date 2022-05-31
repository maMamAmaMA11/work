import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import Storage, ReadyWeight, Rangesort, ReadyRangesort
from .forms import StorageForm, RegisterForm, LoginForm, SearchForm, RangesortForm


# Create your views here.




def index(request):
    return render(request, 'index.html')



#Register/Login


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password,)
                user.save()
                return redirect('login')

        else:
            return redirect('register')
    else:
        registerform = RegisterForm
        return render(request, 'register.html', {"form": registerform})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return redirect ('login')
    else:
        loginform = LoginForm
        return render(request, 'login.html', {"form": loginform})

def logout(request):
    auth.logout(request)
    return redirect('/')


def storage(request):
    if request.method == 'POST':
        search = request.POST['search']
        storages = Storage.objects.filter(name = search)
        searchform = SearchForm()
        data = {"storages": storages, "form": searchform}
        return render(request, 'storage.html', context=data)
    storages = Storage.objects.all()
    searchform = SearchForm()
    data = {"storages": storages, "form": searchform,}
    return render(request, 'storage.html', context=data)

def storage_ordered(request):
    storages = Storage.objects.order_by('name')
    data = {"storages": storages}
    return render(request, 'storage.html', context=data)



def storage_filtrated(request):
    storages = Storage.objects.filter(price__lte = 5)
    data = {"storages": storages}
    return render(request, 'storage.html', context=data)





def storage_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        size = request.POST['size']
        price = request.POST['price']

        storage = Storage.objects.create(name=name, size=size, price=price)
        storage.save()
        return redirect('storage')
    else:
        storageform = StorageForm
        return render(request, 'storage_create.html', {"form": storageform})


def rangesort(request):
    if request.method == 'POST':
        storage1 = request.POST['storage1']
        storage2 = request.POST['storage2']
        storage3 = request.POST['storage3']
        storage4 = request.POST['storage4']
        if storage1 or storage2 or storage3 or storage4:
            rangesort = RangesortForm()
            return render(request, 'rangesort.html', {"form": rangesort})
        storage = Rangesort.objects.create(storage1=storage1, storage2=storage2, storage3=storage3, storage4=storage4)
        storage.save()
        rangesort = RangesortForm()
        return render(request, 'rangesort.html', {"form": rangesort})
    else:
        rangesort = RangesortForm()
        return render(request, 'rangesort.html', {"form": rangesort})

def rangesortresult(request):
    w1 = 0
    w2 = 0
    w3 = 0
    w4 = 0
    rangesort = Rangesort.objects.all()
    weight = ReadyWeight.objects.all()
    weight.delete()
    for rang in rangesort:
        math = rang.storage1 + rang.storage2 + rang.storage3 + rang.storage4
        weight1 = rang.storage1 / math
        weight2 = rang.storage2 / math
        weight3 = rang.storage3 / math
        weight4 = rang.storage4 / math
        weight = ReadyWeight.objects.create(weight1=weight1, weight2=weight2, weight3=weight3, weight4=weight4)
        weight.save()
    weight = ReadyWeight.objects.all()
    wtotal = 0
    wtotal2 = 0
    wtotal3 = 0
    wtotal4 = 0
    for w in weight:
        wtotal += w.weight1
        w1 += 1
        wtotal2 += w.weight2
        w2 += 1
        wtotal3 += w.weight3
        w3 += 1
        wtotal4 += w.weight4
        w4 += 1
    w1result = wtotal/w1
    w2result = wtotal2/w2 
    w3result = wtotal3/w3 
    w4result = wtotal4/w4
    result = ReadyRangesort.objects.all()
    result.delete()
    result = ReadyRangesort.objects.create(w1result=w1result, w2result=w2result, w3result=w3result, w4result=w4result)
    result.save()
    resultview = ReadyRangesort.objects.all()
    data = {"resultview": resultview}
    return render(request, 'result.html', context=data)

