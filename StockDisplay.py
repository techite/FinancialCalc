from urllib2 import Request, urlopen
from urllib import urlencode
def techrequest(symbol, stat):
    #Defining Function that fetches Yahoo Finance CSV 
    url='http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (symbol, stat)
    req = Request(url)
    resp = urlopen(req)
    #Fetching Required Variables 
    content = resp.read().decode().strip()
    return content
y = raw_input('Enter stock name') 
# Script by Techite Solutions (Shashi Prakash Agarwal & Kanak Sharma) 
#symbol= raw_input('Enter Symbol') - Tried testing by accepting manual input
#print techrequest(y,symbol) - Tried testing output from manual input of fetched variable 
o = float(techrequest(y,'o'))
#Setting open 
print ('Open:',o)
h = float(techrequest(y,'h'))
#Setting high
print ('high:',h)
l = float(techrequest(y,'g'))
#Setting last closed value
print ('low:',l)
c = float(techrequest(y,'p'))
#Setting low, 
print ('close:',c) 
#Setting Close. 
