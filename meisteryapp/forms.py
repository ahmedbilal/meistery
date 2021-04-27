from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "first_name", "last_name", "username", "email", "password1", "password2", "is_staff", "is_active", "is_superuser"
        )

    def save(self, commit=True):
        user = super().save(commit)
        return user


class UpdateProductInfoForm(forms.Form):
    user = forms.ModelChoiceField(get_user_model().objects.exclude(is_superuser=True))
    product_info = forms.CharField(widget=forms.widgets.Textarea)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "username", "email", "is_staff", "is_active", "is_superuser", "product_sold")
    password = None