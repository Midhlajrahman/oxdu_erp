from django.contrib import admin
from .models import Application, Examination
from import_export.admin import ImportExportActionModelAdmin


@admin.register(Application)
class ApplicationAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'hallticket_id', 'mobile', 'dob', 'educational_qualification')
    list_filter = ('educational_qualification',)
    search_fields = ('name', 'place', 'mobile', 'email')


@admin.register(Examination)
class ExaminationAdmin(ImportExportActionModelAdmin):
    list_display = ('title', 'date', 'time', 'duration', 'course', 'language')
    list_filter = ('course', 'language')
    search_fields = ('title', 'course', 'language')