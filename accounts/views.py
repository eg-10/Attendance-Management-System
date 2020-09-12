from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


import pandas as pd

from uploads.forms import CSVUploadForm
from accounts.models import Student


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/index.html'

    def get_context_data(self, **kwargs):
        students_count = Student.objects.all().count()
        context = super().get_context_data(**kwargs)
        context['students_count'] = students_count
        return context


class StudentsListView(ListView):
    model = Student
    template_name = 'accounts/students-list.html'