# -*- coding: utf-8 -*-
"""
Display basic information about the last week's Astronomy picture of the day
only show title, description, and concept tags of images
lq and hq urls are shown to view if one sounds like an interesting image to view

@author: Mike Rocco
"""

from datetime import datetime, timedelta
import urllib.request, json

#find the date one week ago
lastweek=datetime.now()-timedelta(days=7)

#url to actually request test data from. replace DEMO_KEY with API key
urlreq="https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&start_date="+lastweek.strftime("%Y-%m-%d")+"&concept_tags=TRUE"

#request for last week's APODs
apodcall=urllib.request.urlopen(urlreq)

#parse into JSON
apodweek=json.load(apodcall)

print("APOD pictures starting from "+lastweek.strftime("%Y-%m-%d"))

#show the title, explanation, concepts, 
for k, v in enumerate(apodweek):
    if apodweek[k]["media_type"] == "image": #only show information for images
        print(apodweek[k]["title"])
        print(apodweek[k]["explanation"])
        print(apodweek[k]["concepts"])
        print("lq URL:"+ apodweek[k]["url"])
        print("hq URL:"+ apodweek[k]["hdurl"])
        print()     #newline
        