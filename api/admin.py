from django.contrib import admin

from import_export import resources
from . models import *

from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.site_header = "BUBT CONVOCATION ADMIN"
admin.site.site_title = "BUBT CONVOCATION"
admin.site.index_title = "API List"

@admin.register(Student)
class StudentInfo(ImportExportModelAdmin, admin.ModelAdmin):    
  #  resource_class = Student
  list_display = ("p_usename","s_id","intake","std_full_name","DOB","Cell_Phone","email")
  pass


admin.site.register(PaymentGatewaySettings)
admin.site.register(ConvocationLogo)
admin.site.register(Convocation)
admin.site.register(ConvocationList)
admin.site.register(Slider)
admin.site.register(chart)
admin.site.register(Transaction)
admin.site.register(Venu)
admin.site.register(Rules)
admin.site.register(ProSchedule)
admin.site.register(CommitteeList)
admin.site.register(Committee)
admin.site.register(Message)
admin.site.register(Speech)
admin.site.register(Gallary)
admin.site.register(OfficeMail)
admin.site.register(Registration)