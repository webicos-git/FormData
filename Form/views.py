from django.shortcuts import render
from django.http import HttpResponse, request
# Create your views here.``
from .models import UserData
from datetime import datetime
from .helpers import save_pdf


def index(request):
    if request.method == 'POST':
        print(request.POST)
        data = request.POST
        server = "Not Selected"
        if "InternationalServer" in data:
            server = "International Server"
        if "AsiaServer" in data:
            server = "Asia Server"

        paymentRecieved = "Not Recieved"
        paymentType = "Not Recieved"
        if "paymentRecieved" in data:
            paymentRecieved = "Payment Recieved"
        if "OnlinePayment" in data:
            paymentType = "Online Payment"
        if "OfflinePayment" in data:
            paymentType = "Offline Payment"
        date = data['date']
        username = data['username']
        clientname = data['clientname']
        profit = data['profit']
        date = datetime.strptime(date, "%Y-%m-%d").strftime('%d-%m-%Y')
        userdata = UserData(username=username, clientname=clientname, profit=profit, date=date,
                            paymentType=paymentType, paymentRecieved=paymentRecieved, server=server)

        userdata.save()
        print("model saved")

    return render(request, 'index.html')


def search(request):
    userdata = UserData.objects.all()
    print(userdata)
    return render(request, 'search.html', {'userdata': userdata})


def getPdf(request):
    params = {'username': 'altamash'}
    filename = save_pdf(params)
    return render(request, 'pdf.html', {'path': filename})

def createPdf(request):
    return render(request, 'pdf.html')