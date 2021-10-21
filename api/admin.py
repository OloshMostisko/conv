from django.contrib import admin

from import_export import resources
from . models import *

from import_export.admin import ImportExportModelAdmin


@admin.register(Student)
class StudentInfo(ImportExportModelAdmin, admin.ModelAdmin):    
  #  resource_class = Student
  list_display = ("p_usename","s_id","intake","std_full_name","Cell_Phone","email")
  pass

