from django.urls import path

from . import views

app_name = "exams"

urlpatterns = [
   path("", views.index, name="index"),
   path("save-application/<str:pk>/", views.save_application, name="save_application"),
   path("application-response/<str:pk>/", views.application_response, name="application_response"),
   path("results/", views.results, name="results"),
]
