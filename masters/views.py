from core import mixins

from . import tables
from .models import State
from django.http import JsonResponse


def get_flights(request):
    airline_id = request.GET.get('airline_id')

    if not airline_id:
        return JsonResponse({'error': 'Airline ID is required.'}, status=400)

    try:
        flights = Flight.objects.filter(is_active=True, airline_id=airline_id).values_list('id', 'flight_number')
        flights_data = [{'id': flight[0], 'flight_number': flight[1]} for flight in flights]
        return JsonResponse({'flights': flights_data}, status=200)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)



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
