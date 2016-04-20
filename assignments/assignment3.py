import urllib2, json, urllib

#http://openstates.org/api/v1/
#bills

#?apikey=1f366e0712bd4ad6b079afe3bb993434

#&state=mo

#&q=firearm

#search_window=session 
#elements become the following url

response = urllib2.urlopen('http://openstates.org/api/v1/bills/?apikey=1f366e0712bd4ad6b079afe3bb993434&state=mo&fields=title,sponsors').read()

dolladollabillsyall = json.loads(response)

for bill in dolladollabillsyall:
    encoded_bill_id = urllib.unquote(bill['sponsors'][0]['name']).encode('utf-8')
    encoded_bill_id2 = urllib.unquote(bill['title']).encode('utf-8')
    print encoded_bill_id, encoded_bill_id2



