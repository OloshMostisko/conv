from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

from django import forms


class PhotoUploadForm(forms.ModelForm):

    class Meta:
        model = Registration
        fields = ('stu_id1', 'p_username', 'intake', 'firstDegree_id', 'photo')