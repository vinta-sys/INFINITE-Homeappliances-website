from django.contrib import admin
from ipend.models import admindb,itemdb,prodb,cartdb,comdb

# Register your models here.
admin.site.register(admindb)
admin.site.register(itemdb)
admin.site.register(prodb)
admin.site.register(cartdb)
admin.site.register(comdb)

