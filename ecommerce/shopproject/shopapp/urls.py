
from django.urls import path
from . import views
app_name='shopapp'
urlpatterns = [

    path('',views.allProdCat,name='allProdCat'),
    path('home/<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prodCatDetail'),
    ]