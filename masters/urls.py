from . import views
from django.urls import path


app_name = "masters"

urlpatterns = [
    # state
    path("state/list/", views.StateListView.as_view(), name="state_list"),
    path("state/<str:pk>/detail/", views.StateDetailView.as_view(), name="state_detail"),
    path("state/create/", views.StateCreateview.as_view(), name="state_create"),
    path("state/<str:pk>/update/", views.StateUpdateView.as_view(), name="state_update"),
    path("state/<str:pk>/delete/", views.StateDeleteView.as_view(), name="state_delete"),
    
    # Course
    path("course/", views.CourseListView.as_view(), name="course_list"),
    path("course/<str:pk>/", views.CourseDetailView.as_view(), name="course_detail"),
    path("new/course/", views.CourseCreateView.as_view(), name="course_create"),
    path("course/<str:pk>/update/", views.CourseUpdateView.as_view(), name="course_update"),
    path("course/<str:pk>/delete/", views.CourseDeleteView.as_view(), name="course_delete"),
]
