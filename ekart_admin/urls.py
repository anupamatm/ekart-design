from django.urls import path
from. import views

app_name = "ekart_admin"

urlpatterns = [   
   path('admin_home',views.admin_home,name="admin_home")
]