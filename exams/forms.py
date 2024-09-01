from .models import Application
from django import forms


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ("name", "place", "mobile", "email", "dob", "educational_qualification")
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Your Name"}
            ),
            "place": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Your Place"}
            ),
            "mobile": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Your Mobile"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Your Email"}
            ),
            "dob": forms.DateInput(
                attrs={"class": "form-control", "placeholder": "Your DOB", "type": "date"}
            ),
            "educational_qualification": forms.Select(
                attrs={"class": "form-control", "placeholder": "Your Educational Qualification"}
            ),
        }