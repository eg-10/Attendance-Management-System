from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

import pandas as pd

from uploads.forms import CSVUploadForm
from accounts.models import Student
from django.contrib.auth.models import User


# class RegisterTeacherView(TemplateView):
#     template_name = ''

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["user_form"] = UserCreationForm()
#         context["teacher_form"] = 

class IndexView(TemplateView):
    template_name = 'accounts/index.html'
