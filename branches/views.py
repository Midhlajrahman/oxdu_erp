from core import mixins
from .models import Branch
from . import tables

class BranchListView(mixins.HybridListView):
    model = Branch
    search_fields = ("name", "email")
    filterset_fields = ("name",)
    table_class = tables.BranchTable
    branch_filter = False


class BranchCreateView(mixins.HybridCreateView):
    model = Branch
    # template_name = "core/branch_form.html"


class BranchUpdateView(mixins.HybridUpdateView):
    model = Branch


class BranchDeleteView(mixins.HybridDeleteView):
    model = Branch
