#PWN_note:  ABC News Webscraper
#PWN_note:  Author: Ru Hickson ru.hickson@gmail.com
#PWN_note:  Created Date:   2018-01-01
#PWN_note:  Updated Date:

#PWN_sect:  Imports
import datetime
import urllib2
from BeautifulSoup import BeautifulSoup

today = str(datetime.date.today())
today = today.replace('-','')

#PWN_sect:  ABC News Headlines
soup = BeautifulSoup(urllib2.urlopen("http://abcnews.go.com/"))
spans = soup.findAll('h1')
lines = [span.getText() for span in spans]
sline = lines[0:]

headline=[]
for i in range(0, len(sline)):
    headline.append("%s" % sline[i])
    i += 1

headlinew = "\n".join(headline)
headlinew = headlinew.encode('utf8')
headlineh = ("\n".join(headline) +"\n")
headlineh = headlineh.encode('utf8')

rep = open("W_ABC_News_"+str(today)+".txt","w+")
rep.writelines(headlinew.replace(' ','\n'))
rep.close()
rep = open("H_ABC_News_"+str(today)+".txt","w+")
rep.writelines(headlineh)
rep.close()

#PWN_note:  End of program