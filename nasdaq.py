#Jan 2024
import requests
import time

#note for FTSE the url is https://www.marketbeat.com/stocks/LON/PRU/
#Europe: https://www.marketbeat.com/stocks/ETR/

def get_stock(nasdaqsym):
    mydata = {}
    if not nasdaqsym:
        return mydata
    myurl = 'https://www.marketbeat.com/stocks/NASDAQ/'+nasdaqsym+'/price-target/'
    #myurl = 'https://www.marketbeat.com/stocks/NASDAQ/AAPL/price-target/'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(myurl, headers=headers)
    content = response.content
    if content:
        #From the phrase disabled title="Share
        p1 = content.find(b'disabled title="Share ')+len('disabled title="Share ')
        p2 = content.find(b' (',p1);
        name = content[p1:p2]
        mydata['name'] = name
        name = name.decode(encoding='UTF-8')
        #print(name)
        #current price
        p3 = content.find(b'<strong>$')+9
        p4 = content.find(b'</strong>')
        price = content[p3:p4]
        price = price.decode(encoding='UTF-8')
        #remove commas
        price = price.replace(',','')
        if price == '':
            return ""
        if len(price) > 20:
            return ""
        mydata['price'] = price
        p5 = content.find(b'Average Forecast</th><td class="text-right">$')+len('Average Forecast</th><td class="text-right">$')
        p6 = content.find(b'<', p5)
        target = content[p5:p6]
        #print("XXX"+str(target))
        target = target.decode(encoding='UTF-8')
        target = target.replace(',','')
        #print(target)
        if len(target) > 20:
            target = ""
        mydata['target'] = target
        fprice = float(price)
        pchange = 0

        try:
            ftarget = float(target)
            pchange = (ftarget - fprice)/fprice * 100
            mydata['pchange'] = pchange
        except:
            pass
        if len(name) < 100:
            print(nasdaqsym+",\""+name+"\","+price+","+target+","+"{:.2f}".format(pchange)+"%")

    return mydata

allsyms=["AAL","AAPL","ADBE","ADI","ADP","ADSK","ALGN","ALXN","AMAT","AMD","AMGN","AMZN","ANSS","ASML","ATVI","AVGO","BIDU","BIIB","BKNG","BMRN","CDNS","CDW","CERN","CHKP","CHTR","CMCSA","COST","CPRT","CSCO","CSGP","CSX","CTAS","CTSH","CTXS","DLTR","EA","EBAY","EXC","EXPE","FAST","META","FOXA","GILD","GOOG","IDXX","ILMN","INCY","INTC","INTU","ISRG","JD","KHC","KLAC","LBTYA","LRCX","LULU","MAR","MCHP","MDLZ","MELI","MNST","MSFT","MU","MXIM","NFLX","NTAP","NTES","NVDA","NXPI","ORLY","PAYX","PCAR","PEP","PYPL","QCOM","REGN","ROST","SBUX","SGEN","SIRI","SNPS","SPLK","SWKS","TCOM","TMUS","TSLA","TTWO","TXN","UAL","ULTA","VRSK","VRSN","VRTX","WBA","WDAY","WDC","WLTW","XEL","XLNX"]
bestp = -99
bests = {}
#print header
print("Symbol,Company,Price,Target,Change")
for sym in allsyms:
    stock = get_stock(sym)
    #print(str(stock))
    if stock and 'pchange' in stock and stock['pchange'] > bestp:
        bestp = stock['pchange']
        bests = stock
    time.sleep(3)
#print("Recommend: "+str(bests))
