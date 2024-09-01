from django.shortcuts import render
from .models import Examination, Application
from .forms import ApplicationForm
from django.http import JsonResponse
from django.shortcuts import redirect


def index(request):
    examinations = Examination.objects.filter(is_active=True)
    form = ApplicationForm(request.POST or None)     
    context = {
        "examinations": examinations,
        "form": form,
    }
    return render(request, "exams/index.html", context)


def save_application(request, pk):
    examination = Examination.objects.get(pk=pk)
    form = ApplicationForm(request.POST or None)
    context = {
        "form": form,
        "exam": examination,
    }
    if request.method == "POST":
        if form.is_valid():
            application = form.save(commit=False)
            application.examination = examination
            application.save()
            redirect_url = redirect("exams:application_response", pk=application.pk)
            response_data = {
                "status": True,
                "redirect": True,
                "redirect_url": redirect_url.url,
                "title": "Success!",
                "message": "Application saved successfully",
            }
        else:
            response_data = {
                "status": False,
                "redirect": False,
                "title": "Error!",
                "message": "Invalid form",
            }
        return JsonResponse(response_data)
    return render(request, "exams/save_application.html", context)
    

def application_response(request, pk):
    application = Application.objects.get(pk=pk)
    return render(request, "exams/application_response.html", {"application": application})


def results(request):
    context = {}
    if request.GET.get("hallticket") and request.GET.get("dob"):
        hallticket_id = request.GET.get("hallticket")
        dob = request.GET.get("dob")
        application = Application.objects.filter(hallticket_id=hallticket_id, dob=dob).first()
        context["application"] = application
    return render(request, "exams/results.html", context)