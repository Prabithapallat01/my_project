from django.shortcuts import render,redirect
from .forms import BrandCreationForm,BrandUpdateForm
from .models import Brands
from .models import Mobile
from .forms import MobileCreationForm
from .forms import UserRegForm
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from .forms import OrderedProduct
from .models import Orders




# Create your views here.
def admin_permission_required(func):
    def wrapper(request):
        if not request.user.is_superuser:
            return redirect("errorpage")
        else:
            return func(request)
    return wrapper

@admin_permission_required
def mobile_create(request):

    form = MobileCreationForm()
    context = {}
    context['form'] = form
    if request.method=="POST":
        form=MobileCreationForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            print("saved")
            return redirect("createmobile")
    return render(request, "mobile/mobcreate.html", context)

def errorpage(request):
    return render(request,'mobile/errorpage.html')



def list_mobile(request):
    mobiles=Mobile.objects.all()
    context={}
    context['mobiles']=mobiles
    for mobile in mobiles:
        print(mobile.mobile_name)
    return render(request,'mobile/listmobiles.html',context)

def admin_permission_required(func):
    def wrapper(request,id):
        if not request.user.is_superuser:
            return redirect("errorpage")
        else:
            return func(request,id)
    return wrapper
@admin_permission_required
def detail_mobile(request,id):
    mobile=Mobile.objects.get(id=id)
    context={}
    context['mobile']=mobile
    return render(request,"mobile/detail.html",context)

def create_brand(request):
    if request.user.is_superuser:
        form=BrandCreationForm()
        context={}
        context['form'] = form
        brands=Brands.objects.all()
        context['brands']=brands
        if request.method=='POST':
            form=BrandCreationForm(request.POST)
            if form.is_valid():
                form.save()
                print("saved")
                return redirect("create")
        return render(request, "mobile/create.html",context)
    else:
        return redirect("errorpage")

def admin_permission_required(func):
    def wrapper(request,id):
        if not request.user.is_superuser:
            return redirect("errorpage")
        else:
            return func(request,id)
    return wrapper
@admin_permission_required
def delete_brand(request,id):
    brand=Brands.objects.get(id=id)
    brand.delete()
    return redirect("create")


def admin_permission_required(func):
    def wrapper(request,id):
        if not request.user.is_superuser:
            return redirect("errorpage")
        else:
            return func(request,id)
    return wrapper
@admin_permission_required
def brand_update(request,id):
    brand=Brands.objects.get(id=id)
    form=BrandUpdateForm(instance=brand)
    context={}
    context['form']=form
    if request.method=='POST':
        form=BrandUpdateForm(request.POST,instance=brand)
        if form.is_valid():
            form.save()
            return redirect("create")

    return render(request,'mobile/update.html',context)


def user_register(request):
    form=UserRegForm()
    context={}
    context['form']=form
    if request.method=='POST':
        form=UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("userlogin")
    return render(request,'mobile/userreg.html',context)

def user_login(request):
    if request.method=="POST":
        username=request.POST.get("uname")
        password=request.POST.get("pwd")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect("listmobiles")
        else:
            return render(request, 'mobile/login.html')

    return render(request, 'mobile/login.html')

def user_logout(request):
    logout(request)
    return redirect("userlogin")




def product_order(request):
    form=OrderedProduct(initial={'user':request.user})
    context={}
    context['form']=form
    if request.method=="POST":
        form=OrderedProduct(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cart")
    return render(request,'mobile/order.html',context)

def cart_items(request):
    user1=request.user
    orders=Orders.objects.all().filter(user=user1)
    context={}
    context['orders']=orders
    return render(request,'mobile/cart.html',context)







