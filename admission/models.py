from datetime import date

from core.base import BaseModel
from django.db import models

from core.choices import BOOL_CHOICES
from core.choices import GENDER_CHOICES
from core.choices import RELIGION_CHOICES
from core.choices import PAYMENT_PERIOD_CHOICES
from core.choices import ATTENDANCE_STATUS

from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone
from djmoney.models.fields import MoneyField
from djmoney.money import Money
from datetime import datetime


def active_objects():
    return {'is_active': True}

class StudentReceipt(BaseModel):
    student = models.ForeignKey("admission.Admission", on_delete=models.PROTECT,related_name = "student")
    academic_year = models.ForeignKey('core.AcademicYear', on_delete=models.PROTECT,null=True)
    receipt_no = models.CharField(max_length=128,null=True)
    date = models.DateField(default=timezone.now)
    transaction_date = models.DateField(null=True,blank=True)
    transaction_refe = models.CharField(max_length=128,blank=True,null=True)
    payment_period = models.CharField(max_length=30, choices=PAYMENT_PERIOD_CHOICES,blank=True,null=True)
    account = models.ForeignKey('accounting.Account', on_delete=models.PROTECT,null=True)
    amount = models.DecimalField(max_digits=14, decimal_places=2, null=True, )
    slip = models.FileField(null=True, blank=True, upload_to="regular/slip/")

    def __str__(self):
        return f"Receipt No: {self.receipt_no} - Student: {self.student} - Amount: {self.amount}"
    
    def total_receipt(self):
        receipts = StudentReceipt.objects.filter(is_active=True, academic_year=self.academic_year, student=self.student,transaction_date__lte=self.transaction_date)
        total_receipt_amount = sum([i.amount for i in receipts])
        return total_receipt_amount 
    
    def balance_due(self):
        admission = self.student
        total_due = admission.tuition_fees - admission.consession_amount - self.total_receipt()
        return total_due

    class Meta:
        ordering = ("-date",)
    
    @staticmethod
    def get_list_url():
        return reverse_lazy("admission:student_receipt_list")

    def get_absolute_url(self):
        return reverse_lazy("admission:student_receipt_detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse_lazy("admission:student_receipt_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("admission:student_receipt_delete", kwargs={"pk": self.pk})
    
    @staticmethod
    def get_student_receipt_report_list_url():
        return reverse_lazy("admission:student_receipt_report_list")

    def get_student_receipt_report_absolute_url(self):
        return reverse_lazy("admission:student_receipt_report_detail", kwargs={"pk": self.pk})
    
    def get_student_receipt_report_create_url(self):
        return reverse_lazy("admission:student_receipt_report_create", kwargs={"pk": self.pk})

    def get_student_receipt_report_update_url(self):
        return reverse_lazy("admission:student_receipt_report_update", kwargs={"pk": self.pk})

    def get_student_receipt_report_delete_url(self):
        return reverse_lazy("admission:student_receipt_report_delete", kwargs={"pk": self.pk})


def generate_admission_no():
    max_ad_no = Admission.objects.aggregate(models.Max('admission_number'))['admission_number__max']
    admission_number = '1' if max_ad_no is None else str(int(max_ad_no) + 1)
    return admission_number.zfill(4)


def generate_admission_fee_receipt_no():
    max_admission_fee_receipt = Admission.objects.aggregate(models.Max('admission_fee_receipt_no'))['admission_fee_receipt_no__max']
    admission_fee_receipt_no = 1 if max_admission_fee_receipt is None else max_admission_fee_receipt + 1
    return admission_fee_receipt_no


class Admission(BaseModel):
    branch = models.ForeignKey("branches.Branch", on_delete=models.PROTECT,null=True)
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE, related_name="student",null=True)
    first_name = models.CharField(max_length=200,null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, blank=True, null=True)
    religion = models.CharField(max_length=20, choices=RELIGION_CHOICES, blank=True, null=True)
    permanent_address = models.TextField(blank=True, null=True)
    communication_address = models.TextField(blank=True, null=True)
    email = models.EmailField(null=True,)
    contact_number = models.CharField(max_length=30,null=True,)
    
    admission_number = models.CharField(max_length=4, null=True, default=generate_admission_no)
    admission_date = models.DateField(default=timezone.now)
    admission_fees = models.DecimalField(max_digits=14, decimal_places=2, null=True)
    admission_fee_receipt_no = models.PositiveIntegerField(default=generate_admission_fee_receipt_no,null=True,)
    academic_year = models.ForeignKey("core.AcademicYear", on_delete=models.CASCADE,null=True,)
    account = models.ForeignKey('accounting.account', on_delete=models.CASCADE, null=True)
    photo = models.FileField(upload_to="admission/documents/", null=True, blank=True)

    # course = models.ForeignKey('web.Course', on_delete=models.CASCADE, limit_choices_to={"is_active": True}, verbose_name="Class to which admission is sought",null=True,)
    batch = models.ForeignKey('admission.Batch',on_delete= models.CASCADE,limit_choices_to={"is_active": True}, null=True, blank=True)
    other_details = models.TextField(blank=True, null=True)

    parent_first_name = models.CharField(max_length=200,null=True,)
    parent_last_name = models.CharField(max_length=200, blank=True, null=True)

    parent_contact_number = models.CharField(max_length=30,null=True, blank=True)
    parent_whatsapp_number = models.CharField(max_length=30, null=True, blank=True)
    parent_mail_id = models.EmailField(verbose_name="Mail Id", null=True, blank=True)
    
    def fullname(self):
        if self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.first_name
    
    def parentfullname(self):
        if self.parent_last_name:
            return f"{self.parent_first_name} {self.parent_last_name}"
        return self.parent_first_name

    def __str__(self):
        return f"{self.fullname()} - {self.admission_number}"

    @staticmethod
    def get_list_url():
        return reverse_lazy("admission:admission_list")

    def get_absolute_url(self):
        return reverse_lazy("admission:admission_detail", kwargs={"pk": self.pk})
    
    # def get_create_url(self):
        # return reverse_lazy("admission:admission_create", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse_lazy("admission:admission_update", kwargs={"pk": self.pk})
    def get_admission_url(self):
        return reverse_lazy("admission:admission_create", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("admission:admission_delete", kwargs={"pk": self.pk})


class Batch(BaseModel):
    academic_year = models.ForeignKey('core.AcademicYear', on_delete=models.CASCADE,blank=True,null=True)
    teacher = models.ForeignKey('employees.Employee', on_delete=models.CASCADE)
    batch_name = models.CharField(max_length=128)
    
    def __str__(self):
        return self.batch_name
    
    @staticmethod
    def get_list_url():
        return reverse_lazy("admission:batch_list")
    
    def get_absolute_url(self):
        return reverse_lazy("admission:batch_detail", kwargs={"pk": self.pk})
    
    def get_create_url(self):
        return reverse_lazy("admission:batch_create", kwargs={"pk": self.pk})
    
    def get_update_url(self):
        return reverse_lazy("admission:batch_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("admission:batch_delete", kwargs={"pk": self.pk})
    

class AcademicYearStudentFee(BaseModel):
    academic_year = models.ForeignKey("core.AcademicYear", on_delete=models.CASCADE)
    student = models.ForeignKey("admission.Admission", on_delete=models.CASCADE)
    course = models.ForeignKey('web.Course', on_delete=models.CASCADE, limit_choices_to={"is_active": True}, verbose_name="Course",null=True,)
    
    def total_receipt(self):
        receipts = StudentReceipt.objects.filter(is_active=True, academic_year=self.academic_year, student=self.student)
        total_receipt_amount = sum([i.amount for i in receipts])
        return total_receipt_amount 
    
    def __str__(self):
        return self.student.fullname()
    
    
    @staticmethod
    def get_list_url():
        return reverse_lazy("admission:academic_year_student_fee_list")

    def get_absolute_url(self):
        return reverse_lazy("admission:academic_year_student_fee_detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse_lazy("admission:academic_year_student_fee_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("admission:academic_year_student_fee_delete", kwargs={"pk": self.pk})
    
    @staticmethod
    def get_fee_detail_list_url():
        return reverse_lazy("admission:fee_detail_list")

    def get_fee_detail_update_url(self):
        return reverse_lazy("admission:fee_detail_update", kwargs={"pk": self.pk})

    def get_fee_detail_delete_url(self):
        return reverse_lazy("admission:fee_detail_delete", kwargs={"pk": self.pk})

    def get_fee_detail_create_url(self):
        return reverse_lazy("admission:fee_detail_create", kwargs={"pk": self.pk})
    
    def get_fee_detail_absolute_url(self):
        return reverse_lazy("admission:fee_detail_detail", kwargs={"pk": self.pk})
    

class AttendanceRegister(BaseModel):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, limit_choices_to=active_objects, null=True)
    date = models.DateField(null=True,)
    
    def __str__(self):
        return f"{self.batch} - {self.date}"
    
    class Meta:
        verbose_name = "Batch Attendance Register"
        verbose_name_plural = "Batch Attendance Registers"
        unique_together = ('batch', 'date',)
        
    def duration(self):
        if self.starting_time and self.ending_time:
            duration = datetime.combine(datetime.min, self.ending_time) - datetime.combine(datetime.min, self.starting_time)
            return duration
        else:
            return None
        
    def get_attendence(self):
        return Attendance.objects.filter(register=self)
    
    def get_total_attendence(self):
        return self.get_attendence().count()
    
    def get_total_present(self):
        return self.get_attendence().filter(status='Present').count()
    
    def get_total_absent(self):
        return self.get_attendence().filter(status='Absent').count()
    

    def get_absolute_url(self):
        return reverse_lazy("admission:attendance_register_detail", kwargs={"pk": self.pk})

    @staticmethod
    def get_list_url():
        return reverse_lazy("admission:attendance_register_list")

    def get_update_url(self):
        return reverse_lazy("admission:attendance_register_update", kwargs={"pk": self.pk})
    
    def get_delete_url(self):
        return reverse_lazy("admission:attendance_register_delete", kwargs={"pk": self.pk})
    
class Attendance(BaseModel):
    register = models.ForeignKey(AttendanceRegister, on_delete=models.CASCADE)
    student = models.ForeignKey(Admission, on_delete=models.CASCADE,limit_choices_to={'is_active': True,})
    status = models.CharField(max_length=30,choices=ATTENDANCE_STATUS)

    def __str__(self):
        return f"{self.student.fullname()} - {self.register.date} - {self.status}"
    

    def get_absolute_url(self):
        return reverse_lazy("admission:attendance_register_detail", kwargs={"pk": self.pk})

    @staticmethod
    def get_list_url():
        return reverse_lazy("admission:attendance_register_list")

    def get_update_url(self):
        return reverse_lazy("admission:attendance_register_update", kwargs={"pk": self.pk})
    
    def get_delete_url(self):
        return reverse_lazy("admission:attendance_register_delete", kwargs={"pk": self.pk})
    
    class Meta:
        ordering = ['id']