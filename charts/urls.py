from django.contrib import admin 
from django.urls import path 
from chartjs import views 
  
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('', views.HomeView.as_view(), name='index'),
    path('top-ten/', views.TopTenUser.as_view(), name='top_ten_user'),
    path('user-profile/', views.UserProfile.as_view(), name='user_profile'),
    path('api', views.ChartData.as_view()), 
] 