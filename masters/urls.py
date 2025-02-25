from . import views
from django.urls import path


app_name = "masters"

urlpatterns = [
    # ajax
    path('get_flights/', views.get_flights, name='get_flights'),
    
    # state
    path("state/list/", views.StateListView.as_view(), name="state_list"),
    path("state/<str:pk>/detail/", views.StateDetailView.as_view(), name="state_detail"),
    path("state/create/", views.StateCreateview.as_view(), name="state_create"),
    path("state/<str:pk>/update/", views.StateUpdateView.as_view(), name="state_update"),
    path("state/<str:pk>/delete/", views.StateDeleteView.as_view(), name="state_delete"),
]
