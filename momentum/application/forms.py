from django import forms
from .models import DIM_BU


class FilterForm(forms.Form):
    business_unit = forms.CharField(max_length=100, required=False)
    category = forms.CharField(max_length=100, required=False)
    product_line = forms.CharField(max_length=100, required=False)
    part_type = forms.CharField(max_length=100, required=False)
    part_number = forms.CharField(max_length=100, required=False)

    brandownername  = forms.CharField(max_length=250, required=False)
    brandname  = forms.CharField(max_length=250, required=False)
    subbrandname  = forms.CharField(max_length=250, required=False)