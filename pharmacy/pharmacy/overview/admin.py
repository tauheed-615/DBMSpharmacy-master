from django.contrib import admin
from .models import *
from company.models import *
from drug.models import *

admin.site.register(CustomUser)
admin.site.register(Pharmacy)
admin.site.register(Drug)
admin.site.register(Company)
admin.site.register(Order)
admin.site.register(UserOrder)
admin.site.register(Stock)
admin.site.register(UserStock)
admin.site.register(StockItem)
admin.site.register(UserStockItem)
admin.site.register(Message)



# Register your models here.
