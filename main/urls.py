from django.urls import path, include
from main import views

urlpatterns = [
    path("", views.MainPageView.as_view(), name='homepage'),
    path('category/<str:slug>/', views.CategoryDetailView.as_view(), name='category'),
    path('recipe-detail/<int:pk>/', views.detail, name='detail'),
    path('add-recipe/', views.add_recipe, name='add_recipe'),
    path('update-recipe/<int:pk>/', views.update_recipe, name='update_recipe'),
    path('delete-recipe/<int:pk>/', views.DeleteRecipeView.as_view(), name='delete_recipe'),
]
