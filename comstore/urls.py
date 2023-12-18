from django.urls import path,include
from . import views
urlpatterns = [
    path('index/',views.index,name='index'),
    path('cart/<int:cartid>',views.cart,name='cart'),
    path('login/',views.log,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logo,name='logout'),
    path('shop/', views.shop, name='shop'),
    path('categories/<int:catid>' ,views.categories,name='categories'),
    path('view_details/<int:vid>',views.view_details,name='view_details'),
    path('showcart/',views.showcart,name="showcart"),
    path('reductcart/<int:cartsub>',views.reductcart,name='reductcart'),
    path('removeitm/<int:delid>',views.removeitm,name='removeitm'),
    path('payment/', views.payment,name='payment'),
    path('orderitem/',views.orderitem,name='orderitem'),
    path('search/',views.search,name='search')
]