from core.base import BaseAdmin

from .models import State
from django.contrib import admin





@admin.register(State)
class StateAdmin(BaseAdmin):
    pass

