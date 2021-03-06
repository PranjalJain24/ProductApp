"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
#from pages import views
#from products import views
from pages.views import home_view,about_view,social_view,contact_view
#from products.views import product_list_view,product_delete_view,dynamic_lookup_view, product_detail_view,product_create_view,render_initial_data

urlpatterns = [
    
    path('products/', include('products.urls')),
    path('Blog/', include('Blog.urls')),
    path('courses/', include('courses.urls')),
    path("",home_view),
    path("home",home_view),
    path("contact",contact_view),
    path("about",about_view),
    path("social",social_view)  
    
]
