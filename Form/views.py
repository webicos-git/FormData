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
        paymentType = ""
        if "paymentRecieved" in data:
            paymentRecieved = "Payment Recieved"
            paymentType = data['paymentmode']

        date = data['date']
        username = data['username']
        clientname = data['clientname']
        date = datetime.strptime(date, "%Y-%m-%d").strftime('%d-%m-%Y')
        transaction = data['buyorsell']
        buy = ""
        sell = ""
        if "buyAmount" in data and data['buyAmount'] != '':
            buy = data['buyAmount']
            buy = float(buy)
        if "sellAmount" in data and data['sellAmount'] != '':
            sell = data['sellAmount']
            sell = float(sell)
        phone = data['phoneNumber']
        userdata = UserData(username=username, clientname=clientname, date=date,
                            paymentType=paymentType, paymentRecieved=paymentRecieved, server=server, transaction=transaction, buyAmount=buy, sellAmount=sell, phone=phone)

        userdata.save()
        print("model saved")
        return render(request, 'index.html', {"message": "Data inserted successfully"})

    return render(request, 'index.html')


def search(request):
    userdata = UserData.objects.all().values()
    # print(userdata)
    return render(request, 'search.html', {'userdata': userdata})


def getPdf(request):
    params = {'userdata': UserData.objects.all()}
    filename, finalProfit, asiaProfit, internationalProfit = save_pdf(params)
    print(filename)
    return render(request, 'pdf.html', {'path': filename, 'userdata': UserData.objects.all(), 'FinalProfit': finalProfit, 'AsiaProfit': asiaProfit, 'IntProfit': internationalProfit})


def createPdf(request):
    return render(request, 'pdf.html')


def deleteUserData(request, id):

    query = UserData.objects.get(id=id)
    query.delete()
    userdata = UserData.objects.all().values()

    return render(request, 'search.html', {'userdata': userdata})
    pass


def downloadReport(request):
    if request.method == 'POST':
        print(request.POST)
        data=request.POST
        customerName=data['customerName']
        date=data['date']
        if len(date)!=0:
            date = datetime.strptime(date, "%Y-%m-%d").strftime('%d-%m-%Y')
        

        month=data['monthfilter']
        monthNew=date[3:5]
        print("date=",date)
        print("month new=",monthNew)


        

    return render(request, 'search.html', {'userdata': UserData.objects.all()})
