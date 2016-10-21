import urllib2, csv
from bs4 import BeautifulSoup

outfile = open('jaildata.csv', 'w')
writer = csv.writer(outfile)

url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'
html = urllib2.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

tbody = soup.find('tbody', {'class': 'stripe'})
rows = tbody.find_all('tr')

for row in rows:
    data = [cell.text for cell in row.find_all('td')[1:]]
    writer.writerow(data)