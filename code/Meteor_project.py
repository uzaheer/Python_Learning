#This program calculates the distance between my current Location and the nearest Meteor Location

#import sys

import requests
import math

def calc_dist(lat1,lon1,lat2,lon2):
	lat1 = math.radians(lat1)
	lon1 = math.radians(lon1)
	lat2 = math.radians(lat2)
	lon2 = math.radians(lon2)

	h = math.sin ((lat2 - lat1) / 2)** 2 + \
	math.cos(lat1) *\
	math.cos(lat2) * \
	math.sin ((lon2 - lon1) /2 ) ** 2 

	return 6372.8 * 2 * math.asin(math.sqrt(h))


def get_dist(meteor):
	return meteor.get('distance',math.inf)

print (calc_dist(50.775000,6.083330,51.509350,-0.595450))

nasa_resp = requests.get('https://data.nasa.gov/resource/gh4g-9sfh.json')

nasa_data = nasa_resp.json()
my_lat = 51.509350
my_long = -0.595450
for nasa_d in nasa_data: 
	if not ('reclat' in nasa_d and 'reclong' in nasa_d): continue
	nasa_d['distance']= calc_dist(float(nasa_d['reclat']),float(nasa_d['reclong']),my_lat,my_long)

nasa_data.sort(key=get_dist)


for n_dist in nasa_data:
	if ('reclat' not in n_dist or 'reclong' not in n_dist): continue
	n_dist['distance'] = calc_dist (float(n_dist['reclat']),float(n_dist['reclong']),my_lat,my_long)
	a = n_dist['name']
	b = n_dist['distance']
	print ('The distance from Slough to {0} is {1} Miles'.format(a,b))
	
