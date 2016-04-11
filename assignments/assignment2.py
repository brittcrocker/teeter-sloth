#(I got way in the weeds on this. I'm pretty lost.)
#(help)
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

countyvalue = 1
countyname = str(countyvalue).zfill(3)

for row in county.find_all('option'):
    html = br.response().read()
    soup = BeautifulSoup(html, "html.parser")
    br.select_form(nr=0) 
    br.form['ctl00$MainContent$cboCounty'] = [countyname]
    br.submit('ctl00$MainContent$btnCountyChange')

    main_table = soup.find('table', {'class', 'electtable'})
    
newname = str(row)
for newname in soup.find_all('option'):
   newname.replaceWith('')


  
    print newname.text
    #for row in main_table.find_all('tr'):
    	#data = [cell.text.encode('utf-8') for cell in row.find_all('td')]
    	#for taco in data:
   
    		#print taco
	 #countyvalue += 2

#for cell in data:
     #candidates = ['Hillary Clinton', 'Bernie Sanders', 'Ted Cruz', 'John R. Kasich', 'Donald J. Trump']
     #percent = ['']
     #print candidates, row, 
