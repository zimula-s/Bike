from django.contrib import admin
from .models import*


class BodaAdmin(admin.ModelAdmin):
    list_display = ("plate_no","model","color")
admin.site.register(Boda,BodaAdmin)

class RiderAdmin(admin.ModelAdmin):
    list_display = ("name","gender","bithdate","contact","email","boda")
admin.site.register(Rider,RiderAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name","gender","bithdate","contact","email")
admin.site.register(Customer,CustomerAdmin)

class TripAdmin(admin.ModelAdmin):
    list_display = ("trip_date","customer","rider","pickup_location","destination","start_time","end_time","amount")
admin.site.register(Trip,TripAdmin)




