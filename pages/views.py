from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.views.generic import edit
from django.urls import reverse_lazy

from .models import UTM_source


class ListView(generic.ListView):
    model = UTM_source
    template_name = "pages/home.html"
    context_object_name = "links"


class DetailView(UserPassesTestMixin, LoginRequiredMixin, generic.DetailView):
    model = UTM_source
    template_name = "pages/link_details.html"
    context_object_name = "link"
    login_url = "account_login"
    
    def test_func(self):
        obj = self.get_object()
        return obj.utm_user == self.request.user

class CreateView(LoginRequiredMixin, edit.CreateView):
    model = UTM_source
    template_name = "pages/link_new.html"
    fields = [
        "utm_url",
        "utm_source",
        "utm_medium",
        "utm_campaign",
        "utm_term",
        "utm_content",
    ]
    login_url = "account_login"

    def form_valid(self, form):
        form.instance.utm_user = self.request.user
        return super().form_valid(form)


class UpdateView(UserPassesTestMixin, LoginRequiredMixin, edit.UpdateView):
    model = UTM_source
    template_name = "pages/link_edit.html"
    fields = [
        "utm_url",
        "utm_source",
        "utm_medium",
        "utm_campaign",
        "utm_term",
        "utm_content",
    ]
    login_url = "account_login"
    
    def test_func(self):
        obj = self.get_object()
        return obj.utm_user == self.request.user


class DeleteView(UserPassesTestMixin, LoginRequiredMixin, edit.DeleteView):
    model = UTM_source
    template_name = "pages/link_delete.html"
    success_url = reverse_lazy("home")
    login_url = "account_login"

    def test_func(self):
        obj = self.get_object()
        return obj.utm_user == self.request.user