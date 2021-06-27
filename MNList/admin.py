from django.contrib import admin
from MNList.models import IBrgy,BResidents,  SBeneficiary, SDistributions, Statusdbs
# Register your models here.

#from .models import IBrgy, Info

admin.site.register(IBrgy)
admin.site.register(BResidents)
admin.site.register(SBeneficiary)
admin.site.register(SDistributions)
admin.site.register(Statusdbs)

