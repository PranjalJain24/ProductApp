
from django.urls import path
#from products import views
from .views import product_list_view,product_delete_view,dynamic_lookup_view, product_detail_view,product_create_view,render_initial_data

app_name = 'products'

urlpatterns = [
    #path("initial",render_initial_data),
    path("<int:id>/",product_detail_view, name="product-detail"),
    path("create/",product_create_view),
    path("",product_list_view, name='product-list'),
    path('<int:id>/delete/',product_delete_view,name='product-delete')
    #path("<int:id>/",dynamic_lookup_view, name='product-detail'),
    
]
