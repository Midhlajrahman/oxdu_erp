from . import views
from django.urls import path


app_name = "admission"

urlpatterns = [
    
    # admission
    path("admissions/", views.AdmissionListView.as_view(), name="admission_list"),
    path("admission/<str:pk>/", views.AdmissionDetailView.as_view(), name="admission_detail"),
    path("new/admission/", views.AdmissionCreateView.as_view(), name="admission_create"),
    path("admission/<str:pk>/update/", views.AdmissionUpdateView.as_view(), name="admission_update"),
    path("admission/<str:pk>/delete/", views.AdmissionDeleteView.as_view(), name="admission_delete"),
    
    # batch
    path("batches/", views.BatchListView.as_view(), name="batch_list"),
    path("batch/<str:pk>/", views.BatchDetailView.as_view(), name="batch_detail"),
    path("new/batch/", views.BatchCreateView.as_view(), name="batch_create"),
    path("batch/<str:pk>/update/", views.BatchUpdateView.as_view(), name="batch_update"),
    path("batch/<str:pk>/delete/", views.BatchDeleteView.as_view(), name="batch_delete"),
    
   
]
