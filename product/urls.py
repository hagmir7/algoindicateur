from django.urls import path
from .views import *



urlpatterns = [
    path('', home, name='home'),
    path('dash', dashboard, name='dashboard'),
    path('product/list', products),
    path('product/create', createProduct),
    path('product/delete/<int:id>', deleteProduct),
    path('product/update/<int:id>', updateProduct),
    path('product/<int:pk>', ProductDetail),
    path('add-to-cart', AdToCart),
    path('cart', cart),
    path('contact', contact),
    path('contact/list', contactList),
    path('contact/<int:id>', message),
    path('products', ourProducts),
    path('benefit/create', createBenefit),
    path('benefit/update/<int:pk>', benefitUpdate),
    path('benefit/list', listBenefit),
    path('benefit/delete/<int:pk>', benefitDelete),

    # Articl
    path('post/create', PostCreate),
    path('post/list', PostList),
    path('post/update/<int:pk>', PostUpdate),
    path('post/delete/<int:pk>', PostDelete),
    path('post/<int:pk>', PostDetail),

    # 
    path('thanks', thanks),
    path('change/language', change_language, name='lang'),


    # Orders
    path("order/all", OrderList),
    path("order/confirmed", OrderConfirmed),
    path("order/canceled", OrderCanceled),
    path("order/cancel", CancelOrder),
    path("order/confirm", ConfirmOrder),
    path("order/new", OrderNew),
]
