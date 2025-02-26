from django.urls import reverse_lazy
from core import mixins

from . import tables
from .forms import CourseForm
from .models import State
from web .models import Course
from django.http import JsonResponse


# def get_flights(request):
#     airline_id = request.GET.get('airline_id')

#     if not airline_id:
#         return JsonResponse({'error': 'Airline ID is required.'}, status=400)

#     try:
#         flights = Flight.objects.filter(is_active=True, airline_id=airline_id).values_list('id', 'flight_number')
#         flights_data = [{'id': flight[0], 'flight_number': flight[1]} for flight in flights]
#         return JsonResponse({'flights': flights_data}, status=200)

#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)



class StateListView(mixins.HybridListView):
    model = State
    table_class = tables.StateTable


class StateDetailView(mixins.HybridDetailView):
    model = State


class StateCreateview(mixins.HybridCreateView):
    model = State


class StateUpdateView(mixins.HybridUpdateView):
    model = State


class StateDeleteView(mixins.HybridDeleteView):
    model = State


class CourseListView(mixins.HybridListView):
    model = Course
    table_class = tables.CourseTable
    filterset_fields = {"course_name": ["icontains"]}
    permissions = ("branch_manager", "teacher", "admin_staff", "is_superuser")
    branch_filter = False
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["can_add"] = True
        context["new_link"] = reverse_lazy("masters:course_create")
        return context
    
    
class CourseDetailView(mixins.HybridDetailView):
    model = Course
    permissions = ("branch_staff", "teacher", "is_superuser",)
    

class CourseCreateView(mixins.HybridCreateView):
    model = Course
    exclude = ("course_name_en", "course_name_ml", "details_en", "details_ml", "description_en", "description_ml", "duration_en", "duration_ml", "fees_en", "fees_ml")
    permissions = ("is_superuser", "teacher", "branch_staff",)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "New Academic Year"
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        return form

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)
    

class CourseUpdateView(mixins.HybridUpdateView):
    model = Course
    # form_class = CourseForm
    exclude = ("course_name_en", "course_name_ml", "details_en", "details_ml", "description_en", "description_ml", "duration_en", "duration_ml", "fees_en", "fees_ml")
    permissions = ("is_superuser", "teacher", "branch_staff", )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Update Academic Year"
        return context
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        return form


class CourseDeleteView(mixins.HybridDeleteView):
    model = Course
    permissions = ("is_superuser", "teacher", "branch_staff", )
