"""attendance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.views import IndexView
from uploads.views import UploadStudentsCSVView, UploadAttendanceCSVView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='home'),
    path('upload-students-csv/', UploadStudentsCSVView.as_view(), name='upload-students-csv'),
    path('upload-attendance-csv/', UploadAttendanceCSVView.as_view(), name='upload-attendance-csv'),
    # path('create-student-accounts/', create_student_accounts, name='create-student-accounts'),
    # path('update-student-attendance/',update_student_attendance,name='update-student-attendance')
]
