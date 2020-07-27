from rest_framework.routers import DefaultRouter
from petshop.core import views
from django.urls import path

app_name = 'core'

router = DefaultRouter()

urlpatterns = [
  path('pets/', views.pet_list),
  path('pets/<int:pet_id>', views.unique_pet),
]