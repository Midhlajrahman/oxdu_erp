from core import mixins
from branches.models import Branch
from core.models import LockingAccount
from core.models import LockingGroup
from core.models import Setting
from branches.tables import BranchTable

from .forms import HomeForm
from .forms import LockingAccountFormSet
from .forms import LockingGroupFormSet
from .forms import SettingForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy


class HomeView(mixins.LoginRequiredMixin, mixins.FormView):
    template_name = "core/home.html"
    form_class = HomeForm
    success_url = reverse_lazy('core:dashboard')

    def get_form(self, *args, **kwargs):
        user = self.request.user
        form = super().get_form(*args, **kwargs)
        if not user.is_superuser:
            form.fields['branch'].initial = user.branch
            form.fields['branch'].queryset = form.fields['branch'].queryset.filter(id=user.branch.id)
        return form

    def form_valid(self, form):
        self.request.session['branch'] = form.cleaned_data['branch'].id
        self.request.session['academic_year'] = form.cleaned_data['academic_year'].id
        return super().form_valid(form)


class DashboardView(mixins.HybridTemplateView):
    template_name = "core/dashboard.html"


class GeneralSettings(mixins.HybridUpdateView):
    model = Setting
    template_name = "core/general_settings.html"
    exclude = None
    form_class = SettingForm

    def get_object(self):
        # Fetch the current branch, assuming the branch is passed in the URL or session
        branch_id = self.request.session.get('branch')  # or self.request.session.get('branch_id')
        branch = get_object_or_404(Branch, id=branch_id)

        # Fetch the single instance of Setting for the current branch or create one if it doesn't exist
        obj, created = self.model.objects.get_or_create(branch=branch)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "General Settings"
        return context

    def get_success_url(self):
        return reverse_lazy('core:general_settings')

    def get_success_message(self, cleaned_data):
        message = "Settings Updated Successfully"
        return message


class GroupSettings(mixins.HybridView):
    template_name = "core/group_settings.html"

    def get(self, request):
        formset = LockingGroupFormSet(queryset=LockingGroup.objects.all())
        context = {"sub_title": "Manage Locking Groups", "title": "Group Settings", "formset": formset}
        return render(request, self.template_name, context)

    def post(self, request):
        formset = LockingGroupFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            messages.success(request, "Locking Groups Updated")
            return redirect("core:group_settings")
        context = {"sub_title": "Manage Locking Groups", "title": "Group Settings", "formset": formset}
        return render(request, self.template_name, context)


class AccountSettings(mixins.HybridView):
    template_name = "core/account_settings.html"

    def get(self, request):
        formset = LockingAccountFormSet(queryset=LockingAccount.objects.all())
        context = {"sub_title": "Manage Locking Accounts", "title": "Account Settings", "formset": formset}
        return render(request, self.template_name, context)

    def post(self, request):
        formset = LockingAccountFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            messages.success(request, "Locking Accounts Updated")
            return redirect("core:account_settings")
        print(formset.errors)
        context = {"sub_title": "Manage Locking Accounts", "title": "Account Settings", "formset": formset}
        return render(request, self.template_name, context)


