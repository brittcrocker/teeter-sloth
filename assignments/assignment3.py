import urllib2, json, urllib
#added urllib to imports to do the code trick demonstrated
#http://openstates.org/api/v1/
#bills

#?apikey=1f366e0712bd4ad6b079afe3bb993434

#&state=mo

#&q=firearm

#search_window=session 
#elements become the following url
#updated url for new assignment
response = urllib2.urlopen('http://openstates.org/api/v1/bills/?apikey=1f366e0712bd4ad6b079afe3bb993434&state=mo&fields=title,sponsors').read()

dolladollabillsyall = json.loads(response)
#honeybooboo yeaaah
#the neat trick
for bill in dolladollabillsyall:
    encoded_bill_id = urllib.unquote(bill['sponsors'][0]['name']).encode('utf-8')
    encoded_bill_id2 = urllib.unquote(bill['title']).encode('utf-8')
    #gimme
    print encoded_bill_id, encoded_bill_id2



