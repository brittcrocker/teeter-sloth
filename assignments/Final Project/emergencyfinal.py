import urllib2, csv, mechanize, re
from bs4 import BeautifulSoup

#writing to csv
outfile = open('finalp1xmll.csv','w')
writer = csv.writer(outfile)

# Write header rows
headers = ['CallDateTime', 'Address', 'ExtNatureDisplayName', 'InNum', 'Timestamp', 'Latitude', 'Longitude', 'Agencies', 'FDids', 'Trucks']
writer.writerow(headers)

# Here we'll grab an XML feed of the data (available by clicking the "GeoRSS Feed" button on the page) rather than HTML
xml = urllib2.urlopen('https://www.como.gov/PSJC/Services/911/911dispatch/fire_georss.php').read()

# Transform the xml into a beautifulsoup object, basically the same as with HTML
soup = BeautifulSoup(xml, "html.parser")

# Find all the item tags
items = soup.find_all('item')

# Loop over them, get the info we want, and write to CSV
for item in items:
    # This is just grabbing all the tags that start with "calldata"
    data = [tag.text.strip() for tag in item.find_all(re.compile("calldata*"))]
    writer.writerow(data)
