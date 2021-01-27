from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import (
            ProductListView,
            ProductCreateView,
            ProductUpdateView,
            ProductPurchaseView,
            ProductDetailView,
            ProductDeleteView,
            ProductByProducer,
            # StoreCreateView
            # StoreListView
        )
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('hispekness/', admin.site.urls),
    path('', ProductListView.as_view(template_name='furn_home.html'), name='home'),
    path('product/<int:pk>', ProductDetailView.as_view( template_name='product/product_detail.html'),  name='product_detail'),
    path('product/new', ProductCreateView.as_view( template_name='product/products_form.html'), name='product_create'),
    path('product/<str:producer>', views.ProductByProducer, name="productsByProducer"),
    path('product/<int:pk>/update', ProductUpdateView.as_view( template_name='product/productupdate_form.html'), name='product_update'),
    path('product/<int:pk>/purchase', ProductPurchaseView.as_view( template_name='product/productpurchase_detail.html'), name='product_purchase'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view( template_name='product/product_confirm_delete.html'), name='product_delete'),
    path('users/login', auth_views.LoginView.as_view( template_name='user/signin.html'), name='login'),
    path('users/logout', auth_views.LogoutView.as_view( template_name='user/logout.html'), name='logout'),
    path('users/', include('user.urls')),
    path('cart', views.cart, name='cart')
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

