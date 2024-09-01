from django.db import models
from django.urls import reverse


class Examination(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    duration = models.IntegerField()
    course = models.ForeignKey("web.Course", verbose_name="Course", on_delete=models.CASCADE)
    language = models.CharField(max_length=100, choices=(("English", "English"), ("Malayalam", "Malayalam")))
    is_active = models.BooleanField(default=True)
    total_marks = models.IntegerField(default=100)
    
    def get_list_url(self):
        return reverse("exams:index")
        
    def get_absolute_url(self):
        return reverse("exams:save_application", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title


class Application(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField()
    educational_qualification = models.CharField(max_length=100)
    examination = models.ForeignKey(Examination, verbose_name="Examination", on_delete=models.CASCADE)
    mark = models.IntegerField(default=0)
    hallticket_id = models.CharField(max_length=100, blank=True, null=True)

    def message(self):
        message_txt = ""
        percentage = (self.mark / self.examination.total_marks) * 100
        if percentage >= 95:
            message_txt = "You are Eligible for 100% Scholarship."
        elif 95 > percentage >=85:
            message_txt = "You are Eligible for 30% Scholarship"
        elif 85 > percentage >=75:
            message_txt = "You are eligible for 20% Scholarship"
        elif 75 > percentage >=50:
            message_txt = "You are not Eligible for Scholarship, but you can pursue the course with full fee"
        else:
            message_txt = "You are not eligible for the Admission this time. However you can Rewrite the Examination when it is available"
        return message_txt

    def __str__(self):
        return self.name