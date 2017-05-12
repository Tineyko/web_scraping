import requests
from BeautifulSoup import BeautifulSoup

url = 'http://quotes.yourdictionary.com/theme/marriage/'

#response = urllib2.urlopen(url).read()

response = requests.get(url)

soup = BeautifulSoup(response.text)

all_quotes = soup.findAll('p', attrs={'class': 'quoteContent'})


count = 0
for single_quote in all_quotes:
    if (count <= 5):
        print single_quote.text
        print "******************"
        count += 1
    else:
        break
