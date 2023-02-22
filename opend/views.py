from django.shortcuts import render, redirect
from ipend.models import itemdb, prodb,admin,comdb,cartdb
from opend.models import registerdb
from django.contrib import messages


# Create your views here.



def homepage(request):
    data = itemdb.objects.all()
    return render(request, "homepage.html", {'data': data})


def about(req):
    data = itemdb.objects.all()
    return render(req, "about.html", {'data': data})


def contact(req):
    data = itemdb.objects.all()
    return render(req, "contact.html", {'data': data})


def discategory(request,itemCatg):
    data = itemdb.objects.all()
    print("===itemcatg===",itemCatg)
    catg=itemCatg.upper()

    products=prodb.objects.filter(category=itemCatg)
    context={
        'products':products,
        'catg':catg,
        'data': data
    }
    return render(request,"discategory.html",context)

def disproduct(request, procatg):
    data = itemdb.objects.all()
    datas = comdb.objects.all()
    print("===procatg===",procatg)
    catgs=procatg.upper()

    things=comdb.objects.filter(productname=procatg)
    context={
        'things':things,
        'catgs':catgs,
        'datas': datas,
        'data':data
    }
    return render(request,"disproduct.html",context)


def details(req, datasid):
    datas=comdb.objects.get(id=datasid)
    messages.success(req, "added to cart")
    return render(req, "details.html",{'datt':datas})


def form(req):
    data = itemdb.objects.all()
    return render(req, "form.html", {'data': data})


def formreg(request):
    if request.method == 'POST':
        na = request.POST.get('username')
        em = request.POST.get('email')
        pa = request.POST.get('password')
        cp = request.POST.get('confirmpassword')
        obj = registerdb(username=na,email=em,password=pa,confirmpassword=cp)
        obj.save()
        messages.success(request, "registered successfully")
        return redirect(form)
    else:
        messages.error(request, "invalid")
        return render(request, "form.html")


def lform(req):
    return render(req, "lform.html")

def customerlogin(request):
    if request.method == 'POST':
        username_r=request.POST.get("username")
        password_r=request.POST.get("password")
        if registerdb.objects.filter(username=username_r,password=password_r).exists():
            request.session['username']=username_r
            request.session['password']=password_r
            messages.success(request, "login successfully")
            return redirect(homepage)
        else:
            messages.error(request, "invalid user")
            return render(request, "form.html")

def customerlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "logout successfully")
    return redirect(form)

def condet(request):
    if request.method == 'POST':
        na = request.POST.get('username')
        em = request.POST.get('email')
        su = request.POST.get('subject')
        me = request.POST.get('message')
        obj = admin(username=na,email=em,subject=su,message=me)
        obj.save()
        messages.success(request, "message sent")
        return redirect(contact)

def cart(req):
    data = itemdb.objects.all()
    return render(req, "cart.html", {'data': data })

def carts(request):
    if request.method == 'POST':
        pn = request.POST.get('companyname')
        na = request.POST.get('username')
        em = request.POST.get('email')
        me = request.POST.get('address')
        su = request.POST.get('phone')
        obj = cartdb(companyname=pn,username=na,email=em,address=me,phone=su)
        obj.save()
        messages.success(request, "order placed")
        return redirect(cart)
