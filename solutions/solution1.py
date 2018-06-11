"""
Exercise 1: Mysterious locations

Examine the data in 'data/exercise1.txt'
The addresses in the file have one thing in common.
Which?
"""

from geopy.geocoders import Nominatim
import time

result = [] 

# go through the file line by line
for line in open('../data/exercise1.txt'):  # <- if this doesnt work try full path
    try:
        address = line.strip()  # cut off newline
        loc = Nominatim().geocode(address)  # get coordinates
        if loc:  # if it works
            # create a line of output
            out = "{}\t{}\t{}\n".format(loc.latitude, loc.longitude, loc.address)
            result.append(out)  # collect in a list
            print(out)
    except GeocoderTimedOut:
        # if the server won't let us in
        print('FAILED:', address)
    time.sleep(3)  # wait 3 sec to avoid the server locking us out

open('result1.txt', 'w').writelines(result)
