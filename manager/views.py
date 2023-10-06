from django.shortcuts import render

def index_view(request):
    return render(request,'index.html')

def boda_view(request):
    return render(request,'boda.html')

def rider_view(request):
    return render(request,'rider.html') 

def customer_view(request):
    return render(request,'customer.html')

def trip_view(request):
    return render(request,'trip.html')


