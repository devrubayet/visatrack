from django import forms

class ReferenceForm(forms.Form):
    reference_number = forms.CharField(max_length=100, label="Reference")
