# -*- coding: utf-8 -*-
"""
Author: njoosse
Date: 2020-06-16

Description: Queries the NOAA API for magnetic declination at a given Latitude, Longitude, Date using Python Requests library
"""

import requests

reqLatitude = 31.129310
reqLongitude = 81.405643
# YYYYMMDD
reqDateStr = '20200615'

def getDeclination(lat, lng, dateStr):
    year = int(dateStr[:4])
    month = int(dateStr[4:6])
    day = int(dateStr[6:])
    
    model = 'WMM'
    resultFormat = 'json'
    
    baseURL = r'https://www.ngdc.noaa.gov/geomag-web/calculators/calculateDeclination'
    backupURL = r'http://magcalc.geomag.info/'
    
    args = []
    args.append('lat1={}'.format(lat))
    args.append('lon1={}'.format(lng))
    args.append('model={}'.format(model))
    args.append('startYear={}'.format(year))
    args.append('startMonth={}'.format(month))
    args.append('startDay={}'.format(day))
    args.append('resultFormat={}'.format(resultFormat))
    
    argsStr = '&'.join(args)
    
    requestURL = baseURL + '?' + argsStr
    print(requestURL)
    
    r = requests.get(requestURL)

    if r.status_code == 200:
        results = r.json()['result'][0]
        units = r.json()['units']
    
    dateYear = results['date']
    elevation = '{} {}'.format(results['elevation'], units['elevation'])
    latitude = '{} {}'.format(results['latitude'], units['latitude'])
    longitude = '{} {}'.format(results['longitude'], units['longitude'])
    declination = '{} {}'.format(results['declination'], units['declination'])
    declination_uncertainty = '{} {}'.format(results['declination_uncertainty'], units['declination_uncertainty'])
    # not a typo, that is what the NOAA returns
    declination_sv = '{} {}'.format(results['declnation_sv'], units['declination_sv'])
    
    return dateYear, elevation, latitude, longitude, declination, declination_uncertainty, declination_sv
    
d, e, lat, lng, dec, dec_un, dec_sv = getDeclination(reqLatitude, reqLongitude, reqDateStr)

