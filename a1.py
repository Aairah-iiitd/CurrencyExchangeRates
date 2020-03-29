#Name: Aairah Bari
#Roll no: 2019003
#Group: 3

def bubblesort(array,size):
    for i in range(size-1):
        for j in range(size-1-i):
            if array[j]>array[j+1]:
                f=array[j]
                array[j]=array[j+1]
                array[j+1]=f

import urllib.request
url=urllib.request.urlopen("https://api.exchangeratesapi.io/latest")
data=url.read()
def getLatestRates():
    """Returns: a JSON string that is a response to a latest rates query.
    The JSON string will have the attributes rates, base and date(yyyy-mm-dd). """

    #print(data)
    return data

def changeBase(amount, currency, desiredCurrency, date):

    """ amount is of type int, currency and desiredCurrency are of type string (INR, USD etc.)
    date is string “yyyy-mm-dd”, return type is float"""
    url=urllib.request.urlopen("https://api.exchangeratesapi.io/"+date+"?base="+desiredCurrency+"&symbols="+currency)
    d = url.read()
    data = str(d)
    a = data.index(":", 11)
    b = data.index("}")
    x = data[a + 1:b]
    factor = float(x)
    return (factor * amount)



def printAscending(json):
        """ Output: the sorted order of the Rates
        Parameter json: a json string to parse
        You don’t have to return anything."""
        temp = str(json)
        temp = temp[12:-36]
        temp = temp.split(',')
        a=len(temp)
        tl=[]
        for i in range(a):
            col= temp[i].find(":")+1
            x= temp[i][col:]
            x=float(x)
            tl.append(x)
        bubblesort(tl,a)
        for i in range(a):
            for j in range(a):
                if (float(temp[j][6:])==tl[i]):
                    print("1 Euro="+str(tl[i])+" "+temp[j][1:4])



import datetime
date = datetime.datetime(2019, 8, 15)


def extremeFridays(startDate, endDate, currency):
    """ Output: on which friday was currency the strongest
    and on which was it the weakest
    You don't have to return anything.
    Parameters: stardDate and endDate are strings of
    the form yyyy-mm-dd
    currency is also a string representing the currency
    whose extremes you have to determine
    """
    url3 = urllib.request.urlopen("https://api.exchangeratesapi.io/history?start_at="+ startDate +"&end_at=" + endDate+ "&symbols=" + currency)
    d = str(url3.read())
    d= d[12:-61]
    tl=d.split(",")
    q =len(tl)
    values=[]
    for i in range(q):
        a=tl[i].find(':')
        b=tl[i].find(":",a+1)
        year=int(tl[i][1:5])
        month=int(tl[i][6:8])
        day=int(tl[i][9:11])
        date=datetime.datetime(year,month,day)
        if (date.weekday()==4):
            values.append(tl[i][b+1:-1])
    bubblesort(values,len(values))
    for i in range(q):
        if (tl[i][20:-1]==values[0]):
            min = tl[i][1:11]
        if (tl[i][20:-1]==values[len(values)-1]):
            max = tl[i][1:11]
    print(currency+" was strongest on "+max+". 1 Euro was equal to "+ values[0]+" "+currency)
    print(currency + " was weakest on " + min + ". 1 Euro was equal to " + values[-1] +" "+ currency)

def findMissingDates(startDate, endDate):
    """ Output: the dates that are not present when you
    do a json query from startDate to endDate
    Parameters: stardDate and endDate are strings of
    the form yyyy-mm-dd"""
    url3 = urllib.request.urlopen("https://api.exchangeratesapi.io/history?start_at=" + startDate + "&end_at=" + endDate)
    s=str(url3.read())
    s=s[12:-63]
    l=s.split("},")
    dategot=[]
    for i in range(len(l)):
        dategot.append(l[i][1:11])
    eDate=datetime.date(int(endDate[0:4]),int(endDate[5:7]),int(endDate[8:]))
    sDate = datetime.date(int(startDate[0:4]), int(startDate[5:7]), int(startDate[8:]))
    x=(eDate+datetime.timedelta(days=1)-sDate).days
    datecal=[]
    for i in range(x):
        datecal.append(sDate+datetime.timedelta(days=i))
    for i in range(len(dategot)):
        year=int(dategot[i][0:4])
        month=int(dategot[i][5:7])
        day=int(dategot[i][8:])
        dategot[i]=datetime.date(year,month,day)
    print("Missing Dates:")
    for i in range(len(datecal)):
        flag=0
        for j in range(len(dategot)):
            if (dategot[j]==datecal[i]):
                flag=1
        if flag==0:
            print(datecal[i])

