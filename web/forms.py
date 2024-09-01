from django import forms

from .models import (
    Branch,
    CareerApplication,
    Contact,
    CourseApplication
)


class ContactForm(forms.ModelForm):
    branch = forms.ModelChoiceField(
        queryset=Branch.objects.all(),
        empty_label="Select Branch",
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
        to_field_name="branch_name",
    )

    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Your Name"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Your Email"}
            ),
            "subject": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Subject"}
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your Message",
                    "rows": "2",
                }
            ),
        }


class CareerForm(forms.ModelForm):
    class Meta:
        model = CareerApplication
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Your Name"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Your Email"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Your Phone Number"}
            ),
            "position": forms.TextInput(
                attrs={"class": "form-control", "readonly": "readonly"}
            ),
            "resume": forms.FileInput(
                attrs={"class": "form-control", "accept": ".pdf, .doc, .docx"}
            ),
        }


class CourseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["branch"].empty_label = "Select Branch"

    class Meta:
        model = CourseApplication
        fields = ["branch", "name", "phone", "place"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Your Name"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Your Phone Number"}
            ),
            "place": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Your Place"}
            ),
            "branch": forms.Select(attrs={"class": "form-control"}),
        }


class BranchCourseForm(forms.ModelForm):

    class Meta:
        model = CourseApplication
        fields = ["name", "phone", "place"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Your Name"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Your Phone Number"}
            ),
            "place": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Your Place"}
            ),
        }
