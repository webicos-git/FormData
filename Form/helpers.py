from io import BytesIO
from django.template.loader import get_template
# import xhtml2pdf.pisa as pisa
from django.conf import settings
from .models import UserData


def save_pdf(params):
    template = get_template('pdf.html')
    html = template.render(params)
    response = BytesIO()
    # pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), response)d
    filename = 'data'

    # logic to calculate profit
    finalProfit = 0
    sellPrice = 0
    asiaProfit = 0
    purchasePrice = 0
    internationalProfit = 0
    userdata = params['userdata']
    print(userdata)
    for field in userdata:
        if field['transaction'] == 'buy':
            purchasePrice += float(field['buyAmount'])
            continue

        if field['transaction'] == 'sell':
            if field['server'] == 'Asia Server':
                asiaProfit += float(field['sellAmount'])*0.4

            elif field['server'] == 'International Server':
                internationalProfit += float(field['sellAmount'])*0.3
            sellPrice += float(field['sellAmount'])

    finalProfit = sellPrice-purchasePrice
    print("Final Profit:", finalProfit)
    print("Asia Profit:", asiaProfit)
    print("International Profit:", internationalProfit)

    template = get_template('pdf.html')
    params['FinalProfit'] = finalProfit
    params['AsiaProfit'] = asiaProfit
    params['IntProfit'] = internationalProfit
    html = template.render(params)
    # response = BytesIO()
    # pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), response)
    # filename = 'data'
    # try:
    #     with open(str(settings.BASE_DIR)+f'\media\{filename}.pdf', 'wb+') as output:
    #         pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), output)

    # except Exception as e:
    #     print(e)

    # if pdf.err:
    #     return '', False

    return f'/media/{filename}.pdf', finalProfit, asiaProfit, internationalProfit
