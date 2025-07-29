from django.urls import path

from .views import CategoryTestView

urlpatterns = [
    # path('/test', CategoriesView.as_view(),name='test'),
     path('test/', CategoryTestView.as_view(), name='test'),
]
