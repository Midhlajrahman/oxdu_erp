from django.db import models
from core.base import BaseModel
from django.urls import reverse, reverse_lazy
from tinymce.models import HTMLField
from versatileimagefield.fields import VersatileImageField



class Course(BaseModel):
    order = models.PositiveIntegerField(null=True, unique=True)
    MODE_CHOICES = [
    ('Online','Online'),
    ('Offline','Offline'),
    ]
    course_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    image = VersatileImageField("Course", upload_to="course/")
    details = models.TextField(null=True, blank=True)
    description = HTMLField(null=True, blank=True)
    seat = models.IntegerField()
    duration = models.CharField(max_length=100)
    fees = models.CharField(max_length=50)
    syllabus = models.FileField(upload_to="syllabus", blank=True, null=True)
    mode =  models.CharField(max_length=128,choices=MODE_CHOICES,blank=True, null=True,default='Offline')
    #meta
    keyword = models.TextField( blank=True, null=True)
    meta_title = models.CharField(max_length=155, blank=True, null=True)
    meta_description = models.CharField(max_length=165, blank=True, null=True)
    
    def __str__(self):
        return self.course_name
    
    class Meta:
        ordering = ("order",)
        
    @staticmethod
    def get_list_url():
        return reverse_lazy("masters:course_list")

    def get_absolute_url(self):
        return reverse_lazy("masters:course_detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse_lazy("masters:course_update", kwargs={"pk": self.pk})
    
    def get_delete_url(self):
        return reverse_lazy("masters:course_delete", kwargs={"pk": self.pk})

    # def get_absolute_url(self):
    #     return reverse("web:course_detail", kwargs={"slug": self.slug})

    def get_points(self):
        return CoursePoint.objects.filter(course=self)


class CoursePoint(models.Model):
    course = models.ForeignKey(
        Course, verbose_name=("Coursepoints"), on_delete=models.CASCADE
    )
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content


class Event(models.Model):
    title = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    image = VersatileImageField(upload_to="freecourse/")
    date = models.DateField()
    start_time = models.TimeField()
    details = models.TextField()
    language = models.CharField(
        max_length=100, choices=(("English", "English"), ("Malayalam", "Malayalam"))
    )
    platform = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)

    def get_absolute_url(self):
        return self.link

    def __str__(self):
        return self.title


class Career(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    branch = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=False)
    description = HTMLField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("web:career_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    person_name = models.CharField(max_length=50)
    image = VersatileImageField("Blog", upload_to="blog/")
    description = HTMLField(null=True, blank=True)
    
    meta_title = models.CharField(max_length=120, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    

    def get_absolute_url(self):
        return reverse("web:update_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class Team(models.Model):
    image = VersatileImageField("Team", upload_to="Team/")
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=200)
    order = models.PositiveIntegerField(null=True, unique=True)

    class Meta:
        ordering = ("order",)

    def __str__(self):
        return self.name


class CareerApplication(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=100, null=True)
    position = models.CharField(max_length=128, null=True)
    resume = models.FileField(upload_to="resume", max_length=500)

    def __str__(self):
        return self.name


class CourseApplication(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=100)
    place = models.CharField(max_length=128, null=True)
    branch = models.ForeignKey(
        "Branch", verbose_name="Branch_course", on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course, verbose_name="Branch_course", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Subscribtion(models.Model):
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.email


class Banner(models.Model):
    banner_head = models.CharField(max_length=50)
    image = models.ImageField(upload_to="banner")
    title = models.CharField(max_length=500)
    content = HTMLField()

    def __str__(self):
        return self.title


class Branch(models.Model):
    meta_title = models.CharField(max_length=120, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    branch_name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=255, unique=True)
    order = models.PositiveIntegerField(unique=True, null=True, blank=True)
    location = models.TextField()
    phone_number = models.CharField(max_length=100)
    whatsapp_number = models.CharField(max_length=100)
    image = VersatileImageField(upload_to="branch/")
    description = HTMLField(null=True, blank=True)
    about_branch = HTMLField("About Branch", null=True, blank=True)

    class Meta:
        ordering = ("order",)
        verbose_name_plural = "Branches"

    def get_absolute_url(self):
        return reverse("web:branch_detail", kwargs={"slug": self.slug})

    def get_courses(self):
        return BranchCourse.objects.filter(branch=self)

    def __str__(self):
        return self.branch_name


class BranchCourse(models.Model):
    meta_title = models.CharField(max_length=120, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    branch = models.ForeignKey(Branch, verbose_name="Branch", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name="Course", on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    image = VersatileImageField(upload_to="course/")
    details = models.TextField()
    description = HTMLField(null=True, blank=True)
    seat = models.IntegerField()
    duration = models.CharField(max_length=10)
    fees = models.CharField(max_length=50)
    syllabus = models.FileField(upload_to="syllabus", blank=True, null=True)

    def get_absolute_url(self):
        return reverse("web:branch_course_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.branch.branch_name


class Testimonial(models.Model):
    person_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="reviewer")
    review = models.TextField()
    branch = models.ForeignKey(Branch, verbose_name="Branch", on_delete=models.CASCADE)

    def __str__(self):
        return self.person_name


class CourseAppointment(models.Model):
    branch_name = models.CharField(max_length=128)
    course = models.ForeignKey(
        Course, verbose_name="Branch_course", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=100, null=True)
    place = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    subject = models.CharField(max_length=128, null=True)
    branch = models.ForeignKey(
        Branch, verbose_name="Branch_course", on_delete=models.CASCADE
    )
    message = models.TextField()

    def __str__(self):
        return self.name


class Endorsement(models.Model):
    name = models.CharField(max_length=128)
    designation = models.CharField(max_length=128)
    media = models.FileField(upload_to="media", max_length=500)

    def is_video(self):
        if self.media.url.endswith(".mp4"):
            return True
        return False

    def __str__(self):
        return self.name


class FAQ(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField()

    def __str__(self):
        return self.question


class Partner(models.Model):
    name = models.CharField(max_length=128)
    logo = models.ImageField(upload_to="partner")

    class Meta:
        verbose_name = "Hiring Partner"
        verbose_name_plural = "Hiring Partners"

    def __str__(self):
        return self.name


class Meta(models.Model):
    meta_title = models.CharField(max_length=120, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    og_title = models.CharField(max_length=120, null=True, blank=True)
    og_description = models.TextField(null=True, blank=True)
    og_image = models.ImageField(upload_to="meta", null=True, blank=True)

    class Meta:
        verbose_name = "Meta Tag"
        verbose_name_plural = "Meta Tags"

    def __str__(self):
        return self.meta_title


class Placement(models.Model):
    name = models.CharField(max_length=128)
    designation = models.CharField(max_length=128)
    place = models.CharField(max_length=128)
    image = models.FileField(upload_to="placed-students/image")

    class Meta:
        verbose_name = "Placement"
        verbose_name_plural = "Placements"

    def __str__(self):
        return self.name


class Certification(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    image = models.FileField(upload_to="certificates/image")

    class Meta:
        verbose_name = "Certification"
        verbose_name_plural = "Certifications"

    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=128)
    image = models.FileField(upload_to="gallery/image")

    class Meta:
        verbose_name = "Galery"
        verbose_name_plural = "Galeries"

    def __str__(self):    
        return self.title
    
class IndexFooterGallery(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="index_footer_gallery")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Index Footer Gallery'
        verbose_name_plural = 'Index Footer Gallery'
    
class BranchImage(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="products/", help_text=" The recommended size is 800x600 pixels."
    )


class BranchFAQ(models.Model):
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
    answer = models.TextField()

    def __str__(self):
        return self.question 

class BranchStory(models.Model):
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=500)
    image = VersatileImageField("story", upload_to="story/")
    
    meta_title = models.CharField(max_length=120, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Branch Story'
        verbose_name_plural = "Branch story"