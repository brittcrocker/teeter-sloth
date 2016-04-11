import urllib2, csv, mechanize
from bs4 import BeautifulSoup


#get the output file ready
output = open('REVISEDassignment2.csv', 'w')
writer = csv.writer(output)

#tell mechanize how to deal with the anonymous form
#def select_form(form) : 
	#return form.attrs.get('id', None) == 'Form1'


#tell mechanize to get the site 
br = mechanize.Browser()
br.open('http://enr.sos.mo.gov/EnrNet/CountyResults.aspx')

#navigate the first drop down 
br.select_form(nr=0) #tell the form what to take
br.form['ctl00$MainContent$cboElectionNames'] = ['750003566'] #tell the form what to take
#submit the form
br.submit('ctl00$MainContent$btnElectionType')
#tell it to get the HTML
html = br.response().read()
# Transform the HTML into a BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

#navigate the Second drop down
countydropdown = soup.find('select', id = 'cboCounty').find_all('option')
counties = []

for i in countydropdown:
	county = {'name':i.text, 'num':i['value']}
	counties.append(county)

	#I GOT THIS PART ABOVE FROM SOMEONE AFTER REALLY NEEDING HELP. CAN SOMEONE EXPLAIN WHAT 'i' HERE IS?

for county in counties:
    br.select_form(nr=0) #tell the form what to take
    br.form['ctl00$MainContent$cboCounty'] = [county['num']] #tell the form what to take
#submit the form
    br.submit('ctl00$MainContent$btnCountyChange')
#tell it to get the html
    html = br.response().read()
#Transform the HTML into a beautifulsoup object
    soup = BeautifulSoup(html, "html.parser")

    #locate the table you want
    main_table = soup.find('table', {'id': 'MainContent_dgrdResults'})

    output=[]
    output.append(county['name'])

    #Find the table
#county = soup.find('select',
	#{'name': 'ctl00$MainContent$cboCounty',
	#'id': 'cboCounty'})

    for row in main_table.find_all('tr'):
        data = [cell.text for cell in row.find_all('td')]
        if data: 
            if data[0] in ['Hillary Clinton', 'Bernie Sanders', 'Ted Cruz', 'John R. Kasich', 'Donald J. Trump']:
                output.append(data[3])
                
    for row in main_table.find_all('tr'):
        data = [cell.text.replace(u'\xa0', '') for cell in row.find_all('td')]
            #countyvalue = 1
            #countyname = str(countyvalue).zfill(3)


#for row in county.find_all('option'):
    #html = br.response().read()
    #soup = BeautifulSoup(html, "html.parser")
    
#newname = str(row)
#for newname in soup.find_all('option'):
    #data = #cell.text.replace(u'\xa0', '')
   # print data
    	#for taco in data:
   
    		#print taco
#for cell in main_table.find_all('tr'):
    #candidates = 
    #percent = ['']
        
#for row in main_table.find_all('tr'):
    #data = [cell.text.encode('utf-8') for cell in row.find_all('td')]
    writer.writerow(data)
