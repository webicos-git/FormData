from django.shortcuts import render
from django.http import HttpResponse, request
# Create your views here.``
from .models import UserData

def index(request):
    if request.method == 'POST':
        print(request.POST)
        data=request.POST
        server=""
        if "InternationalServer" in data:
            server="International Server"
        if "AsiaServer" in data:
            server="Asia Server"
        
        paymentRecieved=""
        paymentType=""
        if "paymentRecieved" in data:
            paymentRecieved="Payment Recieved"
        if "OnlinePayment" in data:
            paymentType="Online Payment"
        if "OfflinePayment" in data:
            paymentType="Offline Payment"
        date=data['date']    
        username=data['username']
        clientname=data['clientname']
        profit=data['profit']

        userdata=UserData(username=username, clientname=clientname, profit=profit,date=date,paymentType=paymentType,paymentRecieved=paymentRecieved,server=server)

        userdata.save()
        print("model saved")
        

        
            
    return render(request,'index.html')

def search(request):
    userdata =UserData.objects.filter(username="admin1")
    print(userdata)
    return render(request,'search.html')    