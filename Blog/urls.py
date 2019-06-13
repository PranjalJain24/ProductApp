from django.urls import path
#from products import views
from .views import ( ArticleListView, 
                    ArticleDetailView,ArticleCreateView, ArticleUpdateView,
                    ArticleDeleteView)

app_name = 'articles'

urlpatterns = [
    path('',ArticleListView.as_view(), name='article-list'),
    path('<int:id>',ArticleDetailView.as_view(), name='article-detail'),
    # path("<int:id>/",product_detail_view, name="product-detail"),
    path("create/",ArticleCreateView.as_view(), name = 'article-create'),
    # path("",product_list_view, name='product-list'),
    path('<int:id>/delete/',ArticleDeleteView.as_view(),name='article-delete'),
    path('<int:id>/update/',ArticleUpdateView.as_view(),name='article-update')
    #path("<int:id>/",dynamic_lookup_view, name='product-detail'),  
]

  
