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
        server = data['server']
        paymentRecieved = "Not Recieved"
        paymentType =""
        if "paymentRecieved" in data:
            paymentRecieved = "Payment Recieved"
            paymentType =data['paymentmode']

       
        date = data['date']
        username = data['username']
        clientname = data['clientname']
        date = datetime.strptime(date, "%Y-%m-%d").strftime('%d-%m-%Y')
        transaction = data['buyorsell']
        buy=""
        sell=""
        if "buyAmount" in data and data['buyAmount'] != '':
            buy=data['buyAmount']
            buy=float(buy)
        if "sellAmount" in data and data['sellAmount'] != '':
            sell=data['sellAmount']
            sell=float(sell)
        userdata = UserData(username=username, clientname=clientname, date=date,
                            paymentType=paymentType, paymentRecieved=paymentRecieved, server=server,transaction=transaction,buyAmount=buy,sellAmount=sell)

        userdata.save()
        print("model saved")

    return render(request, 'index.html')


def search(request):
    #userdata = UserData.objects.all()
    #print(userdata)
    return render(request, 'search.html')

def getPdf(request):
    params = {'username': 'altamash'}
    filename = save_pdf(params)
    return render(request, 'pdf.html', {'path': filename})

def createPdf(request):
    return render(request, 'pdf.html')