#python 2.7.15
import time
import urllib2

#sunarthsh pou dinei ton kwdika html sto programma
def gethtml(url):
    try:
        req = urllib2.Request(url)
        return urllib2.urlopen(req).read()
    except Exception, e:
        time.sleep(2)
        return 'false'
urll = raw_input("Dwste url(xwris to http://):")
url = "http://" + urll
txt = gethtml(url)

from HTMLParser import HTMLParser

#arxikopoihsh twn counter gia th metrhsh twn allagwn grammwn kai twn link
tagcounter = 0
linkcounter = 0

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'p' or tag == 'br' :
            global tagcounter
            tagcounter += 1
        if tag == 'a' or tag == 'link' :
            global linkcounter
            linkcounter += 1

parser = MyHTMLParser()
parser.feed(txt)

#ektypwsh apotelesmatwn
print 'Yparxoun',tagcounter ,'allages grammwn kai',linkcounter,'link'
print 'sto website', url
