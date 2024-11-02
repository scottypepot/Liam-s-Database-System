from django import forms
from .models import Leave

class LeaveForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', max_length=100, required=True)
    last_name = forms.CharField(label='Last Name', max_length=100, required=True)

    class Meta:
        model = Leave
        fields = ['leave_type', 'start_date', 'end_date', 'reason']
        labels = {
            'leave_type': 'Type of Leave',
            'start_date': 'Date of Leave (From)',
            'end_date': 'Date of Leave (To)',
            'reason': 'Reason',
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }