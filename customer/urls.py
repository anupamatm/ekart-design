from django.urls import path
from. import views

app_name = "customer"

urlpatterns = [   
   path('customer_home',views.customer_home, name='customer_home'),
   path('store',views.store,name='store'),
   path('product_detail',views.product_detail,name='product_detail'),
   path('cart',views.cart,name='cart'),
   path('place_order',views.place_order,name='place_order'),
   path('order_complete',views.order_complete,name='order_complete'),
   path('dashboard',views.dashboard,name='dasboard')
   

]