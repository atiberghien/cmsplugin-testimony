from django.contrib import admin
from django import forms
from djangocms_text_ckeditor.widgets import TextEditorWidget
from .models import Testimony

class TestimonyAdminForm(forms.ModelForm):
    class Meta:
        model = Testimony
        widgets = {
          'story': TextEditorWidget(),
        }
        fields = '__all__'

class TestimonyAdmin(admin.ModelAdmin):
    form = TestimonyAdminForm


admin.site.register(Testimony, TestimonyAdmin)
