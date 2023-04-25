from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.db import IntegrityError
from django.contrib import messages
from .models import Product


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        obj = Product.objects.all()
        context = {'object': obj}
        return render(request, 'index.html', context)

    else:
        return redirect('login')


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        result = authenticate(username=username, password=password)
        print(result)
        if result is not None:
            login(request, result)
            return redirect('home')
        else:
            messages.warning(request, "Please enter valid credentials")

    return render(request, 'login.html')


def signupUser(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            usersinfo = User.objects.all()
            for obj in usersinfo:
                if (obj.username == username):
                    messages.warning(request, "Username already exists")
                    return redirect('signup')
                elif (obj.email == email):
                    messages.warning(request, "Email already exists")
                    return redirect('signup')
                elif (password1 != password2):
                    messages.warning(request, "Passwords didnot match")
                    return redirect('signup')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.save()
                    return redirect('login')

    except IntegrityError:
        return redirect('signup')

    return render(request, 'signup.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


def cart(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        product = Product.objects.filter(id=product_id)
        item = product[0]
        content = {
            'product': item,
        }
    return render(request, 'cart.html', content)


def checkout(request):
    if request.method == "GET":
        product_id = request.GET.get('product_id')
        quantity = request.GET.get('quantity')
        product_query = Product.objects.filter(id=product_id)
        actual_product = product_query[0]
        total_cost = actual_product.price * float(quantity)
        context = {
            'product': actual_product,
            'total_cost': total_cost,
            'quantity': quantity
        }
        return render(request, 'checkout.html', context)


def addItem(request):
    if request.method == "POST":
        if request.user.is_superuser:
            title = request.POST.get('title')
            desc = request.POST.get('desc')
            img = request.FILES['img']
            price = float(request.POST.get('price'))
            item = Product(title=title, desc=desc, img=img, price=price)
            item.save()
            return redirect('home')
        else:
            messages.warning(request,"only verified users can add items")
            return redirect('additem')

    return render(request,'additem.html')

def deleteitem(request):
    if request.user.is_superuser:
        if request.method == "POST":
            product_id = request.POST.get('product_id')
            product = Product.objects.filter(id = product_id)
            item = product[0]
            context = {
                'product': item
            }
            return render(request,'deleteitem.html',context)
    else:
        messages.warning(request,'only admins can delete items')
        return redirect('home')

def confirmdelete(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        item = Product.objects.filter(id = product_id)
        item.delete()
        messages.success(request,'item has been deleted succesfully')
        return redirect('home')
def edititem(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        item = Product.objects.filter(id = product_id)
        product = item[0]
        context = {
            'product': product,
        }
        return render(request,'edititem.html',context)
    if request.method == 'POST':
        id = request.POST.get('id')
        title = request.POST.get('title')
        desc  = request.POST.get('desc')
        price = request.POST.get('price')
        img = request.FILES['img']
        item = Product.objects.filter(id=id)
        product = item[0]
        product.title = title
        product.desc = desc
        product.price = price
        product.img = img
        product.save()
        messages.success(request,"Item edited successfully")
        return redirect('home')


