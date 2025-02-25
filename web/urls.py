from django.conf.urls.i18n import set_language
from django.urls import path

from . import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("courses/", views.course, name="course"),
    path("updates/", views.updates, name="updates"),
    path("events/", views.events, name="events"),
    path("careers/", views.careers, name="careers"),
    path("contact/", views.contact, name="contact"),
    path("subscription/", views.subscription, name="subscription"),
    path("branches/", views.branches, name="branches"),
    path("update/<str:slug>/", views.update_detail, name="update_detail"),
    path("course/<str:slug>/", views.course_detail, name="course_detail"),
    path("career/<str:slug>/", views.career_detail, name="career_detail"),
    path("career/success/<str:slug>/", views.career_success, name="career_success"),
    path("branch/<str:slug>/", views.branch_detail, name="branch_detail"),
    path(
        "branch/course/<str:slug>/",
        views.branch_course_detail,
        name="branch_course_detail",
    ),
    path("set_language/", set_language, name="set_language"),
    path("placements/", views.placement, name="placement"),
    path("certifications/", views.certification, name="certification"),
    path("gallery/", views.gallery, name="gallery"),
    # authenticaion
    # path("login/", views.login, name="login"),
    # path("register/", views.register, name="register"),
]
