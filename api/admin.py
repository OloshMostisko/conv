from django.contrib import admin
from django.utils.html import format_html
from import_export import resources
from . models import *

from import_export.admin import ExportActionModelAdmin, ImportExportModelAdmin
# Register your models here.
admin.site.site_header = "BUBT CONVOCATION ADMIN"
admin.site.site_title = "BUBT CONVOCATION"
admin.site.index_title = "API List"

@admin.register(Student)
class StudentInfo(ImportExportModelAdmin, admin.ModelAdmin):    
  #  resource_class = Student
  search_fields = ("p_usename","s_id","intake","std_full_name","DOB","Cell_Phone","email")
  list_display = ("p_usename","s_id","intake","std_full_name","DOB","Cell_Phone","email")
  pass

@admin.register(Registration)
class RegistrationInfo(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ("stu_id1","stu_name","p_username","intake","Cell_Phone","tran_id","totalPaid","secondDegree_id")
    list_display = ("stu_id1","stu_name","p_username","intake","Cell_Phone","tran_id","totalPaid","secondDegree_id","photo")
    pass

@admin.register(Transaction)
class TransactionInfo(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ("sid","name","tran_id","card_type","store_amount","card_no","bank_tran_id","status","tran_date")
    list_display = ("sid","name","tran_id","card_type","store_amount","card_no","bank_tran_id","status","tran_date","card_issuer","card_brand","currency_rate")
    pass
admin.site.register(PaymentGatewaySettings)
admin.site.register(ConvocationLogo)
admin.site.register(Convocation)
admin.site.register(ConvocationList)
admin.site.register(Slider)
admin.site.register(chart)
admin.site.register(Venu)
admin.site.register(Rules)
admin.site.register(ProSchedule)
admin.site.register(CommitteeList)
admin.site.register(Committee)
admin.site.register(Message)
admin.site.register(Speech)
admin.site.register(Gallary)
admin.site.register(OfficeMail)
#admin.site.register(Registration)
admin.site.register(Hosturl)
