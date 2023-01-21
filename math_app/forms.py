#from django.shortcuts import redirect ,render, get_object_or_404, get_list_or_404
from django.forms import ModelForm
from math_app.models import Zscore

class ZScoreForm(ModelForm):
    class Meta:
        model = Zscore
        fields = ('mean', 'std', 'val', 'z')
