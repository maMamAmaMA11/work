from django.contrib import admin
from .models import Storage, Rangesort, ReadyWeight, ReadyRangesort

# Register your models here.

admin.site.register(Storage)
admin.site.register(Rangesort)
admin.site.register(ReadyWeight)
admin.site.register(ReadyRangesort)

