import sys;
import ystockquote;
name = raw_input('Enter name of stock')
price=ystockquote.get_price(name)
o=float(ystockquote.get_today_open(name))
h=float(ystockquote.get_todays_high(name))
l=float(ystockquote.get_todays_low(name))
c=float(ystockquote.get_previous_close(name))
p=(h+c+l)/3
r3=h+2*(p-l)
r1=2*p-l
s1=2*p-h
r2=p+(r1-s1)
s2=p-(r1-s1)
s3=l-2*(h-p)
print ('Current price of '+name+' is '+price)
print ('Resistances are:')
print (r1,r2,r3)
print ('Supports are:')
print (s1,s2,s3)
