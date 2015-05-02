__author__ = 'Legendary Pegasus'
import urllib2
import re
import locale
import json


###########################################################################################################################

#proxy = urllib2.ProxyHandler({'http': '192.168.64.98:809'})
#opener = urllib2.build_opener(proxy)
#urllib2.install_opener(opener)


rate=60

usarray={}
usarray['hundred']=100
usarray['thousand']=1000
usarray['million']=1000000
usarray['billion']=1000000000
usarray['trillion']=1000000000000


#'arab','kharab','neel','padam','shankh'
indarray=['hundred','thousand','lakh','crore']

####this function checks whether a string is a float or not
def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

####this function substitues the matched part with the converted part
#####matched parts are called by re.sub one by one
def slugify(matchObj):
  conv=""
  str = matchObj.group(2)

  #  after removing commas
  str=re.sub(r'[,$]',"",str)
  value=1

  print str



#convert words into numbers based on the value stored in dictionary
  array=re.split(r'\s',str)
  for element in array:
      if isFloat(element):
          value=value*float(element)
      elif element.isalpha():
          if element.lower() in usarray.keys():
              value=value*usarray[element.lower()]
          else:
              conv=element+" "+conv




  #get coverted value from the original value

  value=value*rate


  print value

  ###############previously I used the locale settings to do conversion
  #locale.setlocale(locale.LC_MONETARY, 'English_India')
  #INRcurrency=locale.currency(value,symbol=True,grouping=True,international=True)
  #INRcurrency=float(INRcurrency)

  #value=float(value)


############################This code parses back the number to string form using the literals thousand lakh and crore
  while value>=1000:
      if value>=10000000:
          conv = "crore "+conv
          value/= 10000000
      elif value>=100000:
          conv="lakh "+conv
          value/=100000
      elif value>=1000:
          conv="thousand "+conv
          value/=1000



##################################this is the final converted string with 2 decimal places precision
  conv="INR "+"{:.2f}".format(value)+" "+conv
  conv=conv.strip()
  print conv

  print '\n'
    #convert into words

  return conv

###########################################################################################################################
#file = open('page_content2.html', 'r')
#page_content=file.read()
#print page_content

#########These are the websites I tested the code on
page = urllib2.urlopen('http://money.cnn.com/2015/03/20/investing/fed-profit-balance-sheet/index.html')
#page = urllib2.urlopen('http://zeenews.india.com/news/world/rare-100-carat-diamond-may-fetch-usd-25-million-at-auction_1570205.html')

page_content = page.read()


###########This website is used for getting the exchange rate
page2 = urllib2.urlopen('http://www.google.com/finance/converter?a=1&from=USD&to=INR')
page_content2 = page2.read()

m = re.search('<span class=bld>(.+?) INR</span>', page_content2)
if m:
    rate = float(m.group(1))

#print rate

#arr = re.findall(r'\$\w+ \w+|USD \w+ \w+|\w+ \w+\bdollar', page_content)

#$50 million, USD 50 million, 50 million dollar
#arr = re.sub(r'USD\s([\d.,]+\s*?\w+)', slugify,page_content)
#arr = re.sub(r'\$([\d.,]+\s*?\w+)', slugify, page_content)

#######The converted page is stored in arr
arr = re.sub(r'(\$|USD\s)([\d.,]+\s*?\w+)', slugify, page_content)

#print len(arr)
#for page in arr:
#    print page

#print arr


#####The converted page is written on local disk
with open('page_content.html', 'w') as fid:
    fid.write(arr)

