from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from . import models


class CourseInline(admin.TabularInline):
    model = models.CoursePoint
    extra = 1


class BranchCourseInline(admin.StackedInline):
    model = models.BranchCourse
    extra = 1


@admin.register(models.Course)
class CourseAdmin(ImportExportActionModelAdmin):
    inlines = [CourseInline]
    list_display = ("course_name",)
    prepopulated_fields = {"slug": ("course_name",)}


@admin.register(models.CareerApplication)
class CareerApplicationAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "position", "email", "phone", "resume")


@admin.register(models.Contact)
class ContactAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "branch", "email", "subject", "message")


@admin.register(models.Event)
class EventAdmin(ImportExportActionModelAdmin):
    list_display = ("title", "venue", "date", "start_time")


@admin.register(models.Career)
class CareerAdmin(ImportExportActionModelAdmin):
    list_display = ("title", "branch", "date")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(models.Blog)
class BlogAdmin(ImportExportActionModelAdmin):
    list_display = ("title", "date", "description")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(models.Testimonial)
class TestimonialAdmin(ImportExportActionModelAdmin):
    list_display = ("person_name", "designation", "review")


@admin.register(models.Team)
class TeamAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "designation")


@admin.register(models.CourseApplication)
class CourseApplicationAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "course", "phone", "place")


@admin.register(models.Subscribtion)
class SubscribtionAdmin(ImportExportActionModelAdmin):
    list_display = ("email",)


@admin.register(models.Banner)
class BannerAdmin(ImportExportActionModelAdmin):
    list_display = ("banner_head", "title")


@admin.register(models.Branch)
class BranchAdmin(ImportExportActionModelAdmin):
    list_display = ("branch_name", "location", "order")
    prepopulated_fields = {"slug": ("branch_name",)}
    inlines = [BranchCourseInline]


@admin.register(models.CourseAppointment)
class CourseAppointmentAdmin(ImportExportActionModelAdmin):
    list_display = ("branch_name", "course", "name", "phone", "email", "place")


@admin.register(models.FAQ)
class FAQAdmin(ImportExportActionModelAdmin):
    list_display = ("question", "answer")


@admin.register(models.Partner)
class PartnerAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "logo")


@admin.register(models.Meta)
class MetaAdmin(ImportExportActionModelAdmin):
    list_display = ("meta_title", "meta_description")


@admin.register(models.Placement)
class PlacementAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "designation")


@admin.register(models.Certification)
class CertificationAdmin(ImportExportActionModelAdmin):
    list_display = ("title",)
