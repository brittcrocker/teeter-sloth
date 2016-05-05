Working with the GeoRSS Feeds I found that the filtering was different. 

On the police dispatch, I could filter for two days and have the correct range in the RSS feed. That was not the case for 911 dispatch files. 

Luckily, I ran the scraper a few times at different hours yesterday and had a 911 file from yesterday. I then set the police date/time range to yesterday and scraped it that way.

I imported both tables into SQLite studio and tried a couple of different joins. 


The first, 

SELECT *
FROM PoliceFinal, emergency final
WHERE CallDateTime = Address

This one I did because I knew my rows were dirty and did not line up with the appropriate columns, but I wanted to test run it before I ran the function for an output file. 

It did not work because I also forgot that both tables had an “Address” field, so SQLite was confused. 

I dropped the PoliceFinal table and reimported it with the correct row placement and then named the address field “Address1” so SQL could differentiate between the two. 

Then I ran the following function successfully: 

SELECT *
FROM PoliceFinal, emergencyfinal
WHERE  Address1 = Address

I got five results where both police and emergency personnel responded to the same address, and by the time codes—it looks like the same events. 

They are as follows: 

1. Two Police units and two ambulance units responded to 4000 Hyde Park (Police first for disturbance, then the ambulance, then another police unit around 30 minutes later). 

—Problem noted—the table seems to have listed the ambulance twice in order to join each police unit to something. So it looks like two ambulances until you look at the Time Code which is down to the second. 

2. A 5:27 AM death at 1705 Starlight dr. appears to have been coded as a medical response for ambulances. For the police, who were dispatched two minutes later at 5:29 AM, it was a death investigation. 

3. A “Quint” firetruck and an ambulances were dispatched to 5812 Brown Station Rd-Co at 7:27 am for a medical response. Police were dispatched at 7:29 AM for an accident (vehicular).

4. At 8:35 am two “quint” firetrucks responded to a vehicle fire at 301 Nebraska Av-Co. At  11:44 PM a police cruiser performed a Traffic Stop at the same address. I’m guessing this was not the same vehicle unless Ghost Rider is in town. 


The latitudes and longitudes match up on the addresses. 

I think this would be a lot more interesting with a more extensive date range. I may keep running this for a week or so this summer and create two mass csv’s and join them just to see what it looks like. 