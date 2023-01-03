
from django import forms
from .models import Applicant

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['name', 'applied_job', 'skills', 'mobile', 'address', 'coverletter', 'cv']