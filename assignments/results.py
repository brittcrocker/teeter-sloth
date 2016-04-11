import csv, mechanize
from bs4 import BeautifulSoup

#get the output file ready
#output = open('output.csv', 'w')
#writer = csv.writer(output)

#tell mechanize how to deal with the anonymous form
def select_form(form) : 
	return form.attrs.get('id', None) == 'Form1'


#tell mechanize to get the site 
br = mechanize.Browser()
br.open('http://enr.sos.mo.gov/EnrNet/CountyResults.aspx')

#tell it to get the HTML
html = br.response().read()

# Transform the HTML into a BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")
#fill out the form
#tell form what to take 
br.select_form(nr=0) 
br.form['ctl00$MainContent$cboElectionNames'] = ['750003566']

#Find the table
county = soup.find('select',
	{'name': 'ctl00$MainContent$cboCounty',
	'id': 'cboCounty'})
countyvalue = 001
for row in county.find_all('option'):
    br.select_form(nr=0) 
    br.form['ctl00$MainContent$cboCounty'] = [str(countyvalue)]
    countyvalue += 2

br.submit('ctl00$MainContent$btnCountyChange')

#tell it to get the HTML
html = br.response().read()

# Transform the HTML into a BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")


# Find the main table using both the "align" and "class" attributes
main_table = soup.find('table',
   {'class', 'electtable'})

# Now get the data from each table row
for row in main_table.find_all('tr'):
    data = [cell.text.encode('utf-8') for cell in row.find_all('td')]
    for x in data:
    	print x

   
# for cell in data:
#     candidates = ['Hillary Clinton', 'Bernie Sanders', 'Ted Cruz', 'John R. Kasich', 'Donald J. Trump']
#     percent = ['']
#     print candidates
