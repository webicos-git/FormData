from django.shortcuts import render, redirect
from django.http import HttpResponse, request
# Create your views here.``
from .models import UserData
from datetime import datetime
from .helpers import save_pdf
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
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
        profit = 0
        interProfit = 0
        if data['buyorsell'] == 'SELL':
            profit = data['profit']

        userdata = UserData(username=username, clientname=clientname, date=date,
                            paymentType=paymentType, paymentRecieved=paymentRecieved,
                            server=server, transaction=transaction, buyAmount=buy,
                            sellAmount=sell, phone=phone, profit=profit)

        userdata.save()
        print("model saved")
        return render(request, 'index.html', {"message": "Data inserted successfully"})

    return render(request, 'index.html')


@login_required(login_url='login')
def search(request):
    userdata = UserData.objects.all().values()
    # print(userdata)
    return render(request, 'search.html', {'userdata': userdata})


@login_required(login_url='login')
def createPdf(request):
    return render(request, 'pdf.html')


@login_required(login_url='login')
def deleteUserData(request, id):

    query = UserData.objects.get(id=id)
    query.delete()
    userdata = UserData.objects.all().values()

    return render(request, 'search.html', {'userdata': userdata})
    pass


@login_required(login_url='login')
def getPdf(request):
    params = {'userdata': UserData.objects.all()}
    filename, finalProfit, asiaProfit, internationalProfit = save_pdf(params)
    print(filename)
    return render(request, 'pdf.html', {'path': filename,
                                        'userdata': UserData.objects.all(), 'FinalProfit': finalProfit,
                                        'AsiaProfit': asiaProfit, 'IntProfit': internationalProfit})


@login_required(login_url='login')
def downloadReport(request):
    if request.method == 'POST':
        data = request.POST
        customerName = data['customerName']
        date = data['date']
        if len(date) != 0:
            date = datetime.strptime(date, "%Y-%m-%d").strftime('%d-%m-%Y')
        month = data['monthfilter']
        userdata = UserData.objects.all().values()
        dateORmonth = []
        finalList = []
        # Nothing selected
        if len(customerName) == 0 and month == '0' and len(date) == 0:
            for user in userdata:
                finalList.append(user)
            params = {'userdata': finalList}
            filename, finalProfit, asiaProfit, internationalProfit, totalSell, totalBuy = save_pdf(
                params)
            myDictionary = {'userdata': finalList, 'FinalProfit': finalProfit,
                            'AsiaProfit': asiaProfit, 'IntProfit': internationalProfit,
                            'TotalBuy': totalBuy, 'TotalSell': totalSell
                            }
            return render(request, 'pdf.html', myDictionary)

        # Only username selected
        if month == '0' and len(date) == 0 and len(customerName) != 0:
            # print("inside only username")
            for user in userdata:
                if user['username'].strip() == customerName.strip():
                    finalList.append(user)
            params = {'userdata': finalList}
            filename, finalProfit, asiaProfit, internationalProfit, totalSell, totalBuy = save_pdf(
                params)
            myDictionary = {'userdata': finalList, 'FinalProfit': finalProfit,
                            'AsiaProfit': asiaProfit, 'IntProfit': internationalProfit,
                            'TotalBuy': totalBuy, 'TotalSell': totalSell
                            }
            return render(request, 'pdf.html', myDictionary)

        # date or month selected
        if len(date) != 0 or month != '0' and len(customerName) == 0:
            # Month Wise filter
            if month != '0':
                for user in userdata:
                    userdate = user['date']
                    userdatamonth = userdate[3:5]
                    if month == userdatamonth:
                        dateORmonth.append(user)

            elif len(date) and month == '0':
                for user in userdata:
                    userdataDate = user['date']
                    if date == userdataDate:
                        dateORmonth.append(user)

            finalList = dateORmonth
            if customerName == '':
                params = {'userdata': finalList}
                filename, finalProfit, asiaProfit, internationalProfit, totalSell, totalBuy = save_pdf(
                    params)
                myDictionary = {'userdata': finalList, 'FinalProfit': finalProfit,
                                'AsiaProfit': asiaProfit, 'IntProfit': internationalProfit,
                                'TotalBuy': totalBuy, 'TotalSell': totalSell
                                }
                return render(request, 'pdf.html', myDictionary)

            params = {'userdata': finalList}
            filename, finalProfit, asiaProfit, internationalProfit, totalSell, totalBuy = save_pdf(
                params)
            myDictionary = {'userdata': finalList, 'FinalProfit': finalProfit,
                            'AsiaProfit': asiaProfit, 'IntProfit': internationalProfit,
                            'TotalBuy': totalBuy, 'TotalSell': totalSell
                            }
            return render(request, 'pdf.html', myDictionary)

        # either username or date/month selected
        if customerName != '' and len(date) != 0 or month != '0':
            sampleList = []
            for user in userdata:
                if user['username'].strip() == customerName.strip():
                    sampleList.append(user)

            params = {'userdata': finalList}
            filename, finalProfit, asiaProfit, internationalProfit, totalSell, totalBuy = save_pdf(
                params)
            myDictionary = {'userdata': finalList, 'FinalProfit': finalProfit,
                            'AsiaProfit': asiaProfit, 'IntProfit': internationalProfit,
                            'TotalBuy': totalBuy, 'TotalSell': totalSell
                            }
            return render(request, 'pdf.html', myDictionary)

        # print(finalList)
    return render(request, 'search.html', {'userdata': finalList})


@login_required(login_url='login')
def update(request, id):
    userdata = UserData.objects.get(id=id)
    print(userdata)
    if request.method == 'POST':
        data = request.POST
        print(data)
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
        buy = 0
        sell = 0
        if "buyAmount" in data and data['buyAmount'] != '':
            print("inside first if")
            buy = data['buyAmount']
            buy = float(buy)
        if "sellAmount" in data and data['sellAmount'] != '':
            print("inside second if")
            sell = data['sellAmount']
            sell = float(sell)
        phone = data['phoneNumber']
        profit = 0
        interProfit = 0
        if data['buyorsell'] == 'SELL':
            profit = data['profit']
        u = UserData.objects.get(id=id)
        u.username = username
        u.clientname = clientname
        u.server = server
        u.paymentRecieved = paymentRecieved
        u.paymentType = paymentType
        u.transaction = transaction
        u.sellAmount = sell
        u.buyAmount = buy
        u.phone = phone
        u.date = date
        u.profit = profit
        u.save()
        userdata = UserData.objects.all()
        return render(request, 'search.html', {'userdata': userdata})

    return render(request, 'update.html', {'userdata': userdata})


def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login_auth(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
