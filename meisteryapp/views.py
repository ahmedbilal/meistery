from django.views import generic
from .forms import CustomUserCreationForm, UpdateProductInfoForm, CustomUserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class AdminStaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class UserCreateView(AdminStaffRequiredMixin, generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "meisteryapp/create_user.html"
    success_url = reverse_lazy("list_user")


class UserUpdateView(AdminStaffRequiredMixin, generic.UpdateView):
    form_class = CustomUserChangeForm
    model = get_user_model()
    template_name = "meisteryapp/create_user.html"
    success_url = reverse_lazy("list_user")


class UserListView(AdminStaffRequiredMixin, generic.ListView):
    model = get_user_model()
    template_name = "meisteryapp/list_user.html"


class UpdateProductInfoView(AdminStaffRequiredMixin, generic.FormView):
    form_class = UpdateProductInfoForm
    template_name = "meisteryapp/update_product_info.html"
    success_url = reverse_lazy("update_product_info")

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        cleaned_data['user'].product_info = cleaned_data['product_info']
        cleaned_data['user'].save()
        return super().form_valid(form)
