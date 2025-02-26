from core.base import BaseTable
import django_tables2 as tables
from django_tables2 import columns

from .models import Admission, Batch

class AdmissionTable(BaseTable):
    created = None
    fullname = columns.Column(verbose_name="Student", order_by="first_name")
    course = columns.Column(verbose_name="Course")
    contact_number = columns.Column(verbose_name="Mob")
    admission_date = columns.Column(verbose_name="Admission Date")
    admission_number = columns.Column(verbose_name="Ad.No", linkify=True)

    class Meta:
        model = Admission
        fields = ("admission_number","admission_date","fullname", "course", "contact_number", "action")
        attrs = {"class": "table border-0 star-student table-hover table-striped"}
        
    
class BatchTable(BaseTable):
    created = None
    academic_year = columns.Column(verbose_name="Academic Year")
    teacher = columns.Column(verbose_name="Teacher")
    batch_name = columns.Column(verbose_name="Batch Name")

    class Meta:
        model = Batch
        fields = ("academic_year", "teacher", "batch_name")
        attrs = {"class": "table border-0 star-student table-hover table-striped"}
        
    