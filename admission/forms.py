from django import forms
from accounts.models import User

from admission.models import Admission,AcademicYearStudentFee

class AdmissionForm(forms.ModelForm):
    student_username = forms.CharField(max_length=100, label="Username")
    student_email = forms.EmailField(required=False, label="Email")
    student_password = forms.CharField(label="Password")

    class Meta:
        model = Admission
        exclude = (
            "creator", 
            "account", 
            "slip",
            "contact_person",
            "attendance_date",
            "is_present",
            "user",
            "email"
        )

    def save(self, commit=True):
        admission = super().save(commit=False)
        admission.user = self.save_user(commit=commit)
        if commit:
            admission.save()

            # Create and save AcademicYearStudentFee instance
            academic_year_fee = AcademicYearStudentFee.objects.create(
                academic_year=admission.academic_year,
                student=admission,
                course=admission.course,
                admission_fee=admission.admission_fees,
            )
            
            # Create and save StudentReceipt instance
            # admission_fee_receipt = StudentReceipt.objects.create(
            #     student=admission,
            #     date=self.cleaned_data['admission_date'],
            #     receipt_no=self.cleaned_data['admission_fee_receipt_no'],
            #     academic_year=admission.academic_year,
            #     payment_period='Admission',
            #     student_receipt_transaction_date=self.cleaned_data['student_receipt_transaction_date'],
            #     student_receipt_transaction_refe=self.cleaned_data['student_receipt_transaction_refe'],
            #     student_receipt_amount=self.cleaned_data['admission_fee'],
            #     slip=self.cleaned_data['admission_slip'],
            # )

        return admission
    
    def save_user(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['student_username'],
            email=self.cleaned_data['student_email'],
            password=self.cleaned_data['student_password'],
            first_name=self.cleaned_data['first_name'],
            usertype='student',  
        )

        if commit:
            user.save()
        return user