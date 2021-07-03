 
from django.contrib import admin
from django.urls import path , include
from .import views
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    
    path('users/', views.UserCrudmixinsView.as_view()),
    path('users/<int:pk>/', views.UserCrudmixinsDetailsView.as_view()),
    path('token/',
         jwt_views.TokenObtainPairView.as_view(),
         name ='token_obtain_pair'),
    path('token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name ='token_refresh'),
]
