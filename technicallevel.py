y=raw_input("Enter name of stock:")
print "This program will help you calculate important technical levels for stocks."
print "To proceed with the calculations, enter the following levels:"
o=int(input("Open:"))
h=int(input("High:"))
l=int(input("Low:"))
c=int(input("Close:"))
# This is a script by Shashi Prkash Agarwal to calculate support, resistance and pivot point of stocks
p=(h+c+l)/3

r3=h+2*(p-l)
r1=2*p-l
s1=2*p-h
r2=p+(r1-s1)
s2=p-(r1-s1)
s3=l-2*(h-p)
print "Stock : ",y
print "Pivot Point : ", str(p)
print "Important Resistances :"
print r1
print r2
print r3
print "Important Supports :"
print (s1)
print (s2)
print (s3)
