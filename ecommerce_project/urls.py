from django.urls import path, include

urlpatterns = [
    path('api/auth/', include('registration.urls')),  # using `auth` app
]
