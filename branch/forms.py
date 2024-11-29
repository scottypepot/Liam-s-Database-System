from django import forms
from .models import Branch

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['location', 'image']

class BranchUpdateForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['name', 'location', 'image']