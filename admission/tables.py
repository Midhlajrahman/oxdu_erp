from core.base import BaseTable
import django_tables2 as tables
from django_tables2 import columns

from .models import Admission


class AdmissionTable(BaseTable):
    action = columns.TemplateColumn(template_name="app/partials/admission_actions.html", orderable=False)
    created = None
    fullname = columns.Column(verbose_name="Student", order_by="first_name")
    course = columns.Column(verbose_name="Class")
    contact_number = columns.Column(verbose_name="Mob")
    admission_date = columns.Column(verbose_name="Admission Date")
    admission_number = columns.Column(verbose_name="Ad.No", linkify=True)

    class Meta:
        model = Admission
        fields = ("admission_number","admission_date","fullname", "course_type", "contact_number", )
        attrs = {"class": "table border-0 star-student table-hover table-striped"}
