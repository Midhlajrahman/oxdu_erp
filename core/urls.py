from . import views
from django.urls import path


app_name = "core"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path('general-settings/', views.GeneralSettings.as_view(), name='general_settings'),
    path('group-settings/', views.GroupSettings.as_view(), name='group_settings'),
    path('account-settings/', views.AccountSettings.as_view(), name='account_settings'),
    # branch
    
]
