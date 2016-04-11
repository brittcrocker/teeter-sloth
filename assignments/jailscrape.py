import csv, mechanize
from bs4 import BeautifulSoup

#get the outputl file ready
output = open('output.csv', 'w')
writer = csv.writer(output)

#get the html out of the page
br = mechanize.Browser()
br.open('https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=1000')
html = br.response().read()

#transform the html into a beautifulsoup object
soup = BeautifulSoup(html, "html.parser")

#find the main table using both the "align" and "class" attributes
main_table = soup.find('table',
    {'align': 'center',
    'class': ['collapse', 'shadow', 'BCSDTable']
})
#now get the data from each row
for row in main_table.find_all('tr'):
    data = [cell.text for cell in row.find_all('td')]
    writer.writerow(data)

    


