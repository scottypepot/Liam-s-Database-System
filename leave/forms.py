from django import forms
from .models import Leave

class LeaveForm(forms.ModelForm):
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
        
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date:
            if start_date > end_date:
                raise forms.ValidationError("The 'From' date cannot be later than the 'To' date.")
        return cleaned_data
    