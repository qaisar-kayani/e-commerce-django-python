from django.urls import path, include

urlpatterns = [
    path('api/categories/', include('categories.urls')),  # using  categories
    path('api/auth/', include('registration.urls')),  # using `auth` app
    path('api/product/', include('products.urls'))
]
