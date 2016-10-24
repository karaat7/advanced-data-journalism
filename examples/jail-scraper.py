import urllib2, csv
from bs4 import BeautifulSoup

# Open file and CSV writer
outfile = open('jaildata.csv', 'w')
writer = csv.writer(outfile)

# Get URL ready
url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'
html = urllib2.urlopen(url).read()
# Set up BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find table body/rows
tbody = soup.find('tbody', {'class': 'stripe'})
rows = tbody.find_all('tr')

# Loop over rows and save data from cells
for row in rows:

    # Here's one way to get all of the data into a list

    # # Get all of the cells (td tags) for each row
    # cells = row.find_all('td')

    # # Create a new empty list to hold the output
    # data = []

    # # Loop over each cell in the row
    # for cell in cells:
    #     # Add the cell's data to the row_data output
    #     data.append(cell.text)

    # Here's another way to do it with list comprehensions
    data = [cell.text for cell in row.find_all('td')[1:]]

    writer.writerow(data)