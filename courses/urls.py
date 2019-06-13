from django.urls import path
#from products import views
from .views import ( 
                    CourseView,
                    CourseListView,
                    CourseCreateView,
                    CourseUpdateView,
                    CourseDeleteView
                    #MyListView
                    #my_fbv 
                    )

app_name = 'courses'

urlpatterns = [
    path('', CourseListView.as_view(), name='courses-list'),
    #path('',my_fbv, name='courses-list'),
    path('<int:id>/',CourseView.as_view(), name='courses-detail'),
    # # path("<int:id>/",product_detail_view, name="product-detail"),
    path("create/",CourseCreateView.as_view(), name = 'courses-create'),
    # # path("",product_list_view, name='product-list'),
    path('<int:id>/delete/',CourseDeleteView.as_view(),name='courses-delete'),
    path('<int:id>/update/',CourseUpdateView.as_view(),name='courses-update')
    # path("<int:id>/",dynamic_lookup_view, name='product-detail'),  
]

  
