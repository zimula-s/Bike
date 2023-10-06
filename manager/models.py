from django.db import models


class Boda(models.Model):
   plate_no = models.CharField(max_length=20)
   model = models.CharField(max_length=20)
   color = models.CharField(max_length=20)
   def _str_(self):
    return f"{self.plate_no}-{self.model}-{self.color}"

class Rider(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    bithdate = models.DateField(auto_now=False, auto_now_add=False)
    contact = models.IntegerField()
    email = models.EmailField()
    boda = models.ForeignKey(Boda,on_delete=models.CASCADE)
    def _str_(self):
     return f"{self.name}-{self.gender}-{self.bithdate}-{self.contact}-{self.email}-{self.boda}"
    
class Customer(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    bithdate = models.DateField(auto_now=False, auto_now_add=False)
    contact = models.CharField(max_length=12)
    email = models.EmailField()
    def _str_(self):
     return f"{self.name}-{self.gender}-{self.bithdate}-{self.contact}-{self.email}"

class Trip(models.Model):
    trip_date = models.DateField(auto_now=False, auto_now_add=False)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    rider = models.ForeignKey(Rider,on_delete=models.CASCADE)
    pickup_location=models.CharField(max_length=30)
    destination=models.CharField(max_length=30)
    start_time=models.TimeField(auto_now=False)
    end_time=models.TimeField(auto_now=False)
    amount=models.IntegerField()
    def _str_(self):
        return f"{self.trip_date}-{self.customer}-{self.rider}-{self.pickup_location}-{self.destination}-{self.start_time}-{self.end_time}-{self.amount}"
