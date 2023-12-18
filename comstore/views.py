from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from . models import *
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    data=Categories.objects.all()
    return render(request,"index.html",{'data':data})
def log(request):
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,"inavalid username or password")
            return redirect("login")
    return render(request,"login.html")
def logo(request):
    logout(request)
    return redirect("index")

def register(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password2=request.POST.get('password2')

        if password==password2:
            if User.objects.filter(username=name).exists():
                messages.info(request,"user already exists")
                print("user already exists")
                return redirect("register")
            else:
                user=User.objects.create_user(username=name,email=email,password=password)
                user.save()
                return redirect("login")
        else:
            messages.info(request,"password does not match")
            print("password does not match")
            return redirect("register")
    return render(request,"register.html")
def shop(request):
    data=Product.objects.all()
    data2 = Categories.objects.all()
    p=Paginator(data,6)
    page_num=request.GET.get("page")
    data_obj= p.get_page(page_num)
    return render(request, "shop.html", {'data2': data2,'data':data_obj,'p':p})
def cart(request,cartid):
    data2=Product.objects.get(id=cartid)
    data3,data4=Cartuser.objects.get_or_create(user=request.user)
    if Item.objects.filter(user=data3,product=data2).exists():
        cartadd=Item.objects.get(user=data3,product=data2)
        cartadd.quantity+=1
        cartadd.save()
    else:
        cartnon=Item(user=data3,product=data2,quantity=1)
        cartnon.save()
    return redirect('showcart')
def reductcart(request,cartsub):
    reducect = Product.objects.get(id=cartsub)
    reducect2=Cartuser.objects.get(user=request.user)
    cartsub=Item.objects.get(user=reducect2,product=reducect)
    cartsub.quantity-=1
    cartsub.save()
    return redirect('showcart')
def showcart(request):
    data=Categories.objects.all()
    user=Cartuser.objects.get(user=request.user) #to get current user in cart#
    item=Item.objects.filter(user=user)
    sum=0
    for i in item:
        sum+=i.quantity*i.product.prdtprice
    return render(request, "cart.html" ,{'item':item, 'data':data, 'sum':sum})
def categories(request,catid):
    data2=Categories.objects.all()
    data=Product.objects.filter(categories=catid)
    return render(request,"categories.html",{'data':data,'data2':data2})
def view_details(request,vid):
    data=Product.objects.filter(id=vid)
    return render(request, "view_details.html",{'data':data})
def removeitm(request,delid):
    Item.objects.filter(id=delid).delete()
    return redirect("showcart")
def payment(request):
    user = Cartuser.objects.get(user=request.user)  # to get current user in cart#
    item = Item.objects.filter(user=user)
    sum = 0
    for i in item:
        sum += i.quantity * i.product.prdtprice
    return render(request,"payment.html" ,{'item': item,'sum':sum})
def orderitem(request):
    data=Orderdetails()
    data.first_name = request.POST.get('first_name')
    data.last_name = request.POST.get('last_name')
    data.address = request.POST.get('address')
    data.state = request.POST.get('state')
    data.postal = request.POST.get('postal')
    data.email = request.POST.get('email')
    data.phone = request.POST.get('phone')
    user = Cartuser.objects.get(user=request.user)  # to get current user in cart#
    item = Item.objects.filter(user=user)
    sum=0
    for i in item:
        sum += i.quantity * i.product.prdtprice
    data.subtotal=sum
    data.save()
    for k in item:
        Orderitem.objects.create(order_details=data,
                                 product=k.product,quantity=k.quantity,
                                 price=k.product.prdtprice)
        prdtdata=Product.objects.filter(id=k.product_id).first() #to take this value as first
        prdtdata.stock=prdtdata.stock-k.quantity
        prdtdata.save()
    user_del = Cartuser.objects.get(user=request.user)  # to get current user in cart#
    Item.objects.filter(user=user_del).delete()
    messages.info(request,"Your Order has been successful")
    return redirect('payment')
def search(request):
    b = None
    if 'search' in request.GET:
        w = request.GET['search']
        b = Product.objects.all().filter(Q(prdtname__icontains=w) | Q(prdtdescription__icontains=w)) #iconatins-to give result as the search input either cap or small , to search complex data simply
        print(("search",w))

    return render(request,"search.html",{'data':b})