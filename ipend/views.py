from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from ipend.models import admindb,itemdb,prodb,admin,comdb,cartdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError



# Create your views here.


def index(request):
    return render(request, "index.html")


def Addadmin(request):
    return render(request, "Addadmin.html")


def SaveAdmin(request):
    if request.method == 'POST':
        na = request.POST.get('Name')
        em = request.POST.get('Email')
        mo = request.POST.get('Mobile')
        us = request.POST.get('Username')
        pa = request.POST.get('Password')
        img = request.FILES['image']
        obj = admindb(Name=na, Email=em, Mobile=mo, Username=us, Password=pa, image=img)
        obj.save()
        messages.success(request, "saved")
        return redirect(Addadmin)

def DisplayAdmin(request):
    data = admindb.objects.all()
    return render(request, "displayadmin.html", {'data': data})

def editadmin(req, dataid):
    data = admindb.objects.get(id=dataid)
    print(data)
    return render(req, "editadmin.html", {'data':data})

def updatedata(request,dataid):
    if request.method== 'POST':
        na = request.POST.get('Name')
        em = request.POST.get('Email')
        mo = request.POST.get('Mobile')
        us = request.POST.get('Username')
        pa = request.POST.get('Password')
        try:
            img=request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file= admindb.objects.get(id=dataid).image
        admindb.objects.filter(id=dataid).update(Name=na, Email=em, Mobile=mo, Username=us, Password=pa, image=file)
        messages.success(request, "updated")
        return redirect(DisplayAdmin)

def deletedata(request, dataid):
    data = admindb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "deleted")
    return redirect(DisplayAdmin)





def categorypage(request):
    return render(request, "categorypage.html")


def saveitem(request):
    if request.method == 'POST':
        na = request.POST.get('Name')
        em = request.POST.get('Description')
        img = request.FILES['image']
        obj = itemdb(Name=na, Description=em, image=img)
        obj.save()
        messages.success(request, "saved")
        return redirect(categorypage)

def displayitem(request):
    data = itemdb.objects.all()
    return render(request, "displayitem.html", {'data': data})

def edititem(req, dataid):
    data = itemdb.objects.get(id=dataid)
    print(data)
    return render(req, "edititem.html", {'data':data})

def updateitem(request,dataid):
    if request.method== 'POST':
        na = request.POST.get('Name')
        em = request.POST.get('Description')
        try:
            img=request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file= itemdb.objects.get(id=dataid).image
        itemdb.objects.filter(id=dataid).update(Name=na, Description=em, image=file)
        messages.success(request, "updated")
        return redirect(displayitem)

def deleteitem(request, dataid):
    data = itemdb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "deleted")
    return redirect(displayitem)


def productpage(request):
    data=itemdb.objects.all()
    return render(request, "productpage.html", {'data':data} )


def saveproduct(request):
    if request.method == 'POST':
        ca = request.POST.get('category')
        pn = request.POST.get('productname')
        pr = request.POST.get('price')
        qu = request.POST.get('quantity')
        em = request.POST.get('description')
        img = request.FILES['image']
        obj = prodb(category=ca,productname=pn,price=pr,quantity=qu, description=em, image=img)
        obj.save()
        messages.success(request, "saved")
        return redirect(productpage)
def displayproduct(request):
    data = prodb.objects.all()
    return render(request, "displayproduct.html", {'data': data})
def editproduct(req, dataid):
    data = prodb.objects.get(id=dataid)
    da = itemdb.objects.all()
    print(data)
    return render(req, "editproduct.html", {'data':data, 'da':da})

def updateproduct(request,dataid):
    if request.method== 'POST':
        ca = request.POST.get('category')
        pn = request.POST.get('productname')
        pr = request.POST.get('price')
        qu = request.POST.get('quantity')
        em = request.POST.get('description')

        try:
            img=request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file= prodb.objects.get(id=dataid).image
        prodb.objects.filter(id=dataid).update(category=ca,productname=pn,price=pr,quantity=qu, description=em, image=file)
        messages.success(request, "updated")
        return redirect(displayproduct)

def deleteproduct(request, dataid):
    data = prodb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "deleted")
    return redirect(displayproduct)


def companyproducts(request):
    data=prodb.objects.all()
    return render(request, "companyproducts.html", {'data':data} )


def savecompany(request):
    if request.method == 'POST':
        ca = request.POST.get('productname')
        pn = request.POST.get('companyname')
        pr = request.POST.get('price')
        qu = request.POST.get('quantity')
        em = request.POST.get('description')
        img = request.FILES['image']
        obj = comdb(productname=ca,companyname=pn,price=pr,quantity=qu, description=em, image=img)
        obj.save()
        messages.success(request, "saved")
        return redirect(companyproducts)
def displaycompany(request):
    data = comdb.objects.all()
    return render(request, "displaycompany.html", {'data': data})
def editcompany(req, dataid):
    data = comdb.objects.get(id=dataid)
    da = prodb.objects.all()
    print(data)
    return render(req, "editcompany.html", {'data': data, 'da': da})

def updatecompany(request,dataid):
    if request.method== 'POST':
        ca = request.POST.get('productname')
        pn = request.POST.get('companyname')
        pr = request.POST.get('price')
        qu = request.POST.get('quantity')
        em = request.POST.get('description')

        try:
            img=request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file= comdb.objects.get(id=dataid).image
        comdb.objects.filter(id=dataid).update(productname=ca,companyname=pn,price=pr,quantity=qu, description=em, image=file)
        messages.success(request, "updated")
        return redirect(displaycompany)

def deletecompany(request, dataid):
    data = comdb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "deleted")
    return redirect(displaycompany)

def loginpage(rqst):
    return render(rqst, "loginpage.html")

def adminlogin(rqst):
    if rqst.method == "POST":
        username_r = rqst.POST.get('username')
        password_r = rqst.POST.get('password')

        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(rqst, user)
                rqst.session['username']=username_r
                rqst.session['password']=password_r
                messages.success(rqst, "login successfully")
                return redirect(index)

            else:
                messages.error(rqst, "invalid user")
                return render(rqst, "loginpage.html")
        else:
            messages.error(rqst, "invalid user")
            return render(rqst, "loginpage.html")
def adminlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "logout successfully")
    return redirect(loginpage)


def admintable(request):
    data = admin.objects.all()
    return render(request, "contactdisplay.html", {'data': data})


def deleteadmin(request, dataid):
    data = admin.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Deleted")
    return redirect(admintable)

def displaycart(request):
    data = cartdb.objects.all()
    return render(request, "displaycart.html", {'data': data})

def deletecart(request, dataid):
    data = cartdb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Deleted")
    return redirect(displaycart)

