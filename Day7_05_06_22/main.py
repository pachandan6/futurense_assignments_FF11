#Regular expression
import re
"""
var="kohli is better than dhoni"
data=re.match("kohli",var) # match is used only to search the first word
print(data.group())

print(data.group())
print(data.span())
print(data.start())  # to get the starting position
print(data.end())    ## to get the ending position

data1=re.search("is",var,re.I) #search is used to search any word in the sentence
print(data1.group())
print(data1.start())  # to get the starting position
print(data1.end())    # to get the ending position
print(data1.span())   # to get the position of the match
"""

var1="""is better than dhoni 
kohli they both play for india
they both are kohli excellent players"""
data2=re.search("they",var1,re.M)
print(data2)

var3="<html><body><head></body>"
data3=re.search("<.*>",var3,re.I)  # greedy search or the deepest search
#print(data3.group())

var4="<html><body><head></body>"
data4=re.search("<.*?>",var4,re.I) # non greedy search
print(data4.group())

var5="kohli is better than dhoni"
data5=re.search("(.*) is (.*) (.*)",var5)
print(data5.group())
print(data5.group(1))
print(data5.group(2))
print(data5.group(3))