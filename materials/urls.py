from django.urls import path, include
from materials import views
from .views import  MaterialsListView, CompListView


urlpatterns = [
    path("materials/", MaterialsListView.as_view(), name='material' ),
    path('compound/', CompListView.as_view(), name='compound'),
    path('compound/create_compound/', views.createcompound, name='create_compound'),
]