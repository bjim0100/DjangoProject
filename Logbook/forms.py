from django import forms
from django.db import models

from bootstrap_modal_forms.forms import BSModalModelForm

from .models import Loginfo, VisitorInfo


class RegistrationModel(BSModalModelForm):
    class Meta:
        model = Loginfo

        fields =[
            'name',
            'department',
            'staff_id',
            'time'


        ]


class VisitorModel(BSModalModelForm):
    class Meta:
        model = VisitorInfo

        fields = [
            'name',
            'visitor_department',
            'visitor_name',
            'time'

        ]