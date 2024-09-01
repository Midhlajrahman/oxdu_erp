import os

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import BranchCourseForm, CareerForm, ContactForm, CourseForm
from .models import (
    FAQ,
    Banner,
    Blog,
    Branch,
    BranchCourse,
    Career,
    Certification,
    Course,
    Event,
    Partner,
    Placement,
    Subscribtion,
    Team,
    Testimonial,
)


def index(request):
    banner = Banner.objects.all()[:1]
    courses = Course.objects.all()
    testimonials = Testimonial.objects.all()
    faqs = FAQ.objects.all()
    events = Event.objects.all()

    context = {
        "is_index": True,
        "courses": courses,
        "testimonials": testimonials,
        "events": events,
        "banners": banner,
        "faqs": faqs,
    }
    return render(request, "web/index.html", context)


def about(request):
    courses = Course.objects.all()
    teams = Team.objects.all()
    partners = Partner.objects.all()
    context = {
        "is_about": True,
        "courses": courses,
        "teams": teams,
        "partners": partners,
    }
    return render(request, "web/about.html", context)


def events(request):
    events = Event.objects.all()
    context = {"is_events": True, "events": events}
    return render(request, "web/events.html", context)


def course(request):
    courses = Course.objects.all()
    context = {"is_course": True, "courses": courses}
    return render(request, "web/course-list.html", context)


def placement(request):
    placements = Placement.objects.all()
    context = {"is_placements": True, "placements": placements}
    return render(request, "web/placements.html", context)


def certification(request):
    certifications = Certification.objects.all()
    context = {"is_certifications": True, "certifications": certifications}
    return render(request, "web/certifications.html", context)


def course_detail(request, slug):
    course = Course.objects.get(slug=slug)
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.course = course
            data.save()
            messages.success(request, "Success! Message sent successfully.")

            if course.syllabus:
                with open(course.syllabus.path, "rb") as pdf_file:
                    response = HttpResponse(
                        pdf_file.read(), content_type="application/pdf"
                    )
                    response["Content-Disposition"] = (
                        "inline; filename=" + os.path.basename(course.syllabus.path)
                    )
                    return response
            else:
                return redirect("web:course")

    else:
        form = CourseForm()
    context = {"course": course, "course_is": str(slug), "form": form}
    return render(request, "web/course-details.html", context)


def branch_course_detail(request, slug):
    course = BranchCourse.objects.get(slug=slug)
    title = "Best Job Oriented Courses | Career-Focused Training at OXDU Integrated Media School"
    if course.meta_title:
        title = course.meta_title
    if request.method == "POST":
        form = BranchCourseForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.course = course.course
            data.branch = course.branch
            data.save()
            messages.success(request, "Success! Message sent successfully.")

            if course.syllabus:
                with open(course.syllabus.path, "rb") as pdf_file:
                    response = HttpResponse(
                        pdf_file.read(), content_type="application/pdf"
                    )
                    response["Content-Disposition"] = (
                        "inline; filename=" + os.path.basename(course.syllabus.path)
                    )
                    return response
            else:
                return redirect("web:course")
    else:
        form = BranchCourseForm()

    context = {
        "course": course,
        "course_is": str(slug),
        "form": form,
        "is_meta": True,
        "title": title,
    }
    return render(request, "web/branch-course-details.html", context)


def careers(request):
    careers = Career.objects.all()
    context = {"is_career": True, "careers": careers}
    return render(request, "web/career.html", context)


def career_detail(request, slug):
    career = Career.objects.get(slug=slug)
    if request.method == "POST":
        form = CareerForm(files=request.FILES or None, data=request.POST or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.position = career
            data.save()
            messages.success(request, "Success! Message sent successfully.")
            return redirect("web:career_success", slug=slug)
        print(form.errors)
    else:
        form = CareerForm(initial={"position": career.title})
    context = {"careers": career, "form": form}
    return render(request, "web/career-details.html", context)


def career_success(request, slug):
    career = Career.objects.get(slug=slug)
    context = {"careers": career}
    return render(request, "web/career-success.html", context)


def updates(request):
    blogs = Blog.objects.all()
    context = {"is_blog": True, "blogs": blogs}
    return render(request, "web/blog.html", context)


def update_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    prev_blog = Blog.objects.filter(id__lt=blog.id).order_by("-id").first()
    next_blog = Blog.objects.filter(id__gt=blog.id).order_by("id").first()
    context = {"blog": blog, "prev_blog": prev_blog, "next_blog": next_blog}
    return render(request, "web/blog-details.html", context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Success! Message sent successfully.")
            return redirect("web:contact")
    else:
        form = ContactForm()
    context = {"is_contact": True, "form": form}
    return render(request, "web/contact.html", context)


def subscription(request):
    if request.method == "POST":
        email = request.POST.get("email")
        subscription = Subscribtion(email=email)
        subscription.save()
        messages.success(request, "succsessfully saved")
        return redirect("web:index")
    return None


def branches(request):
    branch = Branch.objects.all()
    context = {
        "is_branch": True,
        "branches": branch,
    }
    return render(request, "web/branches.html", context)


def branch_detail(request, slug):
    branch = Branch.objects.get(slug=slug)
    testimonials = Testimonial.objects.filter(branch=branch)
    form = ContactForm(request.POST)
    title = "Best Job Oriented Courses | Career-Focused Training at OXDU Integrated Media School"
    if branch.meta_title:
        title = branch.meta_title
    if form.is_valid():
        data = form.save(commit=False)
        data.branch = branch
        data.save()
        messages.success(request, "Success! Message sent successfully.")
        return redirect("web:branches")
    else:
        form = ContactForm(initial={"branch": branch})
        form.fields["branch"].queryset = Branch.objects.filter(slug=slug)
    context = {
        "is_branch": True,
        "branch": branch,
        "form": form,
        "testimonials": testimonials,
        "is_meta": True,
        "title": title,
    }
    return render(request, "web/branch-details.html", context)


def login(request):
    return render(request, "web/sign-in.html")


def register(request):
    return render(request, "web/sign-up.html")
