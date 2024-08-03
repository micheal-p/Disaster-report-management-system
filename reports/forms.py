from django import forms
from .models import Report

DISASTER_TYPE_CHOICES = [
    ('earthquake', 'Earthquake'),
    ('flood', 'Flood'),
    ('hurricane', 'Hurricane'),
    ('wildfire', 'Wildfire'),
    ('tornado', 'Tornado'),
    # Add other disaster types as needed
]

class ReportForm(forms.ModelForm):
    disaster_type = forms.ChoiceField(choices=DISASTER_TYPE_CHOICES)

    class Meta:
        model = Report
        fields = ['disaster_type', 'location', 'description', 'image']
