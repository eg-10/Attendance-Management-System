import io
import pandas as pd

from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from accounts.models import Student
from uploads.forms import CSVUploadForm
# def create_student_accounts(request):
#     print('files',request.FILES)
#     print('get',request.GET)
#     if request.FILES['csv-file']:
#         df = pd.read_csv(request.FILES['csv-file'])
#         columns = list(df.columns)
#         for values in df.values.tolist():
#             d = dict(zip(columns,values))
#             u = User.objects.create(
#                 username=d['uid'],
#                 password='SPIT@'+d['uid'],
#                 email=d['email'],
#                 first_name=d['first_name'],
#                 last_name=d['last_name'])
#             Student.objects.create(user=u,uid=d['uid'])
#         return HttpResponse('SUCCESS')

# def update_student_attendance(request):
#     if request.FILES['csv-file']:
#         df = pd.read_csv(request.FILES['csv-file'])
#         columns = list(df.columns)
#         for values in df.values.tolist():
#             d = dict(zip(columns,values))
#             try:
#                 Student.objects.get(uid=d['uid']).update(attendance=d['attendance'])
#             except:
#                 continue
#         return HttpResponse('SUCCESS')

class UploadStudentsCSVView(FormView):
    template_name = 'uploads/upload-students-csv.html'
    form_class = CSVUploadForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        f = io.TextIOWrapper(form.cleaned_data['csv_file'].file)
        df = pd.read_csv(f)
        columns = list(df.columns)
        for values in df.values.tolist():
            d = dict(zip(columns,values))
            try:
                s = Student.objects.get(uid=str(d['uid']))
            except:
                u = User.objects.create_user(
                    username=str(d['uid']),
                    password='SPIT@'+str(d['uid']),
                    email=d['email'],
                    first_name=d['first_name'],
                    last_name=d['last_name'])
                Student.objects.create(user=u,uid=str(d['uid']))
        return super().form_valid(form)


class UploadAttendanceCSVView(FormView):
    template_name = 'uploads/upload-attendance-csv.html'
    form_class = CSVUploadForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        f = io.TextIOWrapper(form.cleaned_data['csv_file'].file)
        df = pd.read_csv(f)
        columns = list(df.columns)
        for values in df.values.tolist():
            d = dict(zip(columns,values))
            try:
                s = Student.objects.get(uid=str(d['uid']))
                s.attendance = str(d['attendance'])
                s.save()            
            except:
                continue
        return super().form_valid(form)
