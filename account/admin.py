from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User
from .utils import for_save

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user = for_save(user, self.cleaned_data["password1"])
        return user
    


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'is_active', 'is_superuser', 'address', 'telephone_number')

    def clean_password(self):
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email','is_superuser')
    list_filter = ('is_superuser',)
    fieldsets = (
        (None, {'fields': ('first_name','last_name','username', 'email', 'password','address', 'telephone_number')}),
        ('Permissions', {'fields': ('is_superuser',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name','last_name','username', 'email', 'password1', 'password2',  'address', 'telephone_number')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()




admin.site.register(User, UserAdmin)

admin.site.unregister(Group)

