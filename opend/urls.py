from django.urls import path
from opend import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('discategory/<itemCatg>/', views.discategory, name="discategory"),
    path('disproduct/<procatg>/', views.disproduct, name="disproduct"),
    path('details/<int:datasid>/',views.details,name="details"),
    path('form/', views.form, name="form"),
    path('formreg/', views.formreg, name="formreg"),
    path('lform/', views.lform, name="lform"),
    path('customerlogin/', views.customerlogin, name="customerlogin"),
    path('customerlogout/', views.customerlogout, name="customerlogout"),
    path('condet/', views.condet, name="condet"),
    path('cart/', views.cart, name="cart"),
    path('carts/', views.carts, name="carts")


]