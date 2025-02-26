from core.base import BaseForm

from django import forms

from web.models import Course


class CourseForm(BaseForm):
    class Meta:
        model = Course
        
        fields = [
            "order", "course_name", "slug", "image", "details", "description",
            "seat", "duration", "fees", "syllabus", "mode",
            "keyword", "meta_title", "meta_description", "is_active"
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
            "details": forms.Textarea(attrs={"rows": 3}),
            "fees": forms.TextInput(attrs={"placeholder": "Enter fee amount"}),
            "duration": forms.TextInput(attrs={"placeholder": "e.g. 6 months"}),
            "slug": forms.TextInput(attrs={"placeholder": "Auto-generated if left blank"}),
            "meta_title": forms.TextInput(attrs={"maxlength": 155}),
            "meta_description": forms.Textarea(attrs={"rows": 2, "maxlength": 165}),
            "keyword": forms.Textarea(attrs={"rows": 2}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Only keep the English language fields
        english_fields = ["course_name", "description", "details", "meta_title", "meta_description", "keyword"]
        self.fields = {key: self.fields[key] for key in english_fields if key in self.fields}

        if not self.instance.pk:
            self.fields["is_active"].initial = True