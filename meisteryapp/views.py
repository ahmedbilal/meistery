from django.views import generic
from .forms import CustomUserCreationForm, UpdateProductInfoForm, CustomUserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

class UserCreateView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "meisteryapp/create_user.html"
    success_url = reverse_lazy("list_user")


class UserUpdateView(generic.UpdateView):
    form_class = CustomUserChangeForm
    model = get_user_model()
    template_name = "meisteryapp/create_user.html"
    success_url = reverse_lazy("list_user")

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs['initial']['product_sold'] = ''
    #     return kwargs

class UserListView(generic.ListView):
    model = get_user_model()
    template_name = "meisteryapp/list_user.html"


class UpdateProductInfoView(generic.FormView):
    form_class = UpdateProductInfoForm
    template_name = "meisteryapp/update_product_info.html"
    success_url = reverse_lazy("update_product_info")

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        cleaned_data['user'].product_info = cleaned_data['product_info']
        cleaned_data['user'].save()
        return super().form_valid(form)