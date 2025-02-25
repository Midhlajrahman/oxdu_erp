from django.shortcuts import render
from django.urls import reverse_lazy
from core import mixins
from admission .models import Admission
from . import tables
from .forms import AdmissionForm


class AdmissionListView(mixins.HybridListView):
    model = Admission
    table_class = tables.AdmissionTable
    filterset_fields = {'first_name': ['icontains'], }
    permissions = ("branch_manager", "teacher", "admin_staff" "is_superuser")
    
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

    
class AdmissionDetailView(mixins.HybridDetailView):
    model = Admission
    permissions = ("branch_staff", "teacher", "is_superuser",)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Admission Details"
        return context
    

class AdmissionCreateView(mixins.HybridCreateView):
    model = Admission
    template_name = 'admission/admission_form.html'
    # form_class = AdmissionForm
    permissions = ("is_superuser", "teacher", "branch_staff", )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "New Admission"
        return context

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)