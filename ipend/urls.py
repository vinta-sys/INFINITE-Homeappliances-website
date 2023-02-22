from django.urls import path
from ipend import views


urlpatterns = [
    path('index/', views.index, name="index"),
    path('Addadmin/', views.Addadmin, name="Addadmin"),
    path('SaveAdmin/', views.SaveAdmin, name="SaveAdmin"),
    path('DisplayAdmin/', views.DisplayAdmin, name="DisplayAdmin"),
    path('editadmin/<int:dataid>/', views.editadmin, name="editadmin"),
    path('updatedata/<int:dataid>/', views.updatedata, name="updatedata"),
    path('deletedata/<int:dataid>/', views.deletedata, name="deletedata"),

    path('categorypage/', views.categorypage, name="categorypage"),
    path('saveitem/', views.saveitem, name="saveitem"),
    path('displayitem/', views.displayitem, name="displayitem"),
    path('edititem/<int:dataid>/', views.edititem, name="edititem"),
    path('updateitem/<int:dataid>/', views.updateitem, name="updateitem"),
    path('deleteitem/<int:dataid>/', views.deleteitem, name="deleteitem"),

    path('productpage/', views.productpage, name="productpage"),
    path('saveproduct/', views.saveproduct, name="saveproduct"),
    path('displayproduct/', views.displayproduct, name="displayproduct"),
    path('editproduct/<int:dataid>/', views.editproduct, name="editproduct"),
    path('updateproduct/<int:dataid>/', views.updateproduct, name="updateproduct"),
    path('deleteproduct/<int:dataid>/', views.deleteproduct, name="deleteproduct"),

    path('companyproducts/', views.companyproducts, name="companyproducts"),
    path('savecompany/', views.savecompany, name="savecompany"),
    path('displaycompany/', views.displaycompany, name="displaycompany"),
    path('editcompany/<int:dataid>/', views.editcompany, name="editcompany"),
    path('updatecompany/<int:dataid>/', views.updatecompany, name="updatecompany"),
    path('deletecompany/<int:dataid>/', views.deletecompany, name="deletecompany"),

    path('loginpage/', views.loginpage, name="loginpage"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),

    path('admintable/', views.admintable, name="admintable"),
    path('deleteadmin/<int:dataid>/', views.deleteadmin, name="deleteadmin"),

    path('displaycart/', views.displaycart, name="displaycart"),
    path('deletecart/<int:dataid>/', views.deletecart, name="deletecart")

]
