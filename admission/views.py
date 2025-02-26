from django.shortcuts import render
from django.urls import reverse_lazy
from core import mixins

from admission .models import Admission, Batch
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
    

class AdmissionCreateView(mixins.HybridCreateView):
    model = Admission
    # form_class = AdmissionForm
    permissions = ("is_superuser", "teacher", "branch_staff", )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "New Admission"
        return context

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)
    

class AdmissionUpdateView(mixins.HybridUpdateView):
    model = Admission
    permissions = ("is_superuser", "teacher", "branch_staff", )


class AdmissionDeleteView(mixins.HybridDeleteView):
    model = Admission
    permissions = ("is_superuser", "teacher", "branch_staff", )


class BatchListView(mixins.HybridListView):
    model = Batch
    table_class = tables.BatchTable
    filterset_fields = {'academic_year': ['exact'], }
    permissions = ("branch_manager", "teacher", "admin_staff" "is_superuser")
    
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

    
class BatchDetailView(mixins.HybridDetailView):
    model = Batch
    permissions = ("branch_staff", "teacher", "is_superuser",)
    

class BatchCreateView(mixins.HybridCreateView):
    model = Batch
    permissions = ("is_superuser", "teacher", "branch_staff", )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "New Batch"
        return context

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)
    

class BatchUpdateView(mixins.HybridUpdateView):
    model = Batch
    permissions = ("is_superuser", "teacher", "branch_staff", )


class BatchDeleteView(mixins.HybridDeleteView):
    model = Batch
    permissions = ("is_superuser", "teacher", "branch_staff", )