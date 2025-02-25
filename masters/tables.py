from core.base import BaseTable

from .models import State




class StateTable(BaseTable):
    class Meta(BaseTable.Meta):
        model = State
        fields = ("name",)
