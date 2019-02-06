import time, urllib2

#sunarthsh pou dinei ton kwdika html sto programma
def gethtml(url):
    try:
        req = urllib2.Request(url)
        return urllib2.urlopen(req).read()
    except Exception, e:
        time.sleep(2)
        return 'false'
url = 'http://www.amarynthos.gr/'
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
print 'There are',tagcounter ,'line breaks and',linkcounter,'links'
print 'in the website www.amarynthos.gr'
