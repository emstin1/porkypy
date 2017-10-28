#!/usr/bin/env python3

'''
 PorkPy:  amateur radio callsign lookup from the commmand line.
 Copyright (C) 2017 Eric M Stinger

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.
 emstin1@protonmail.com
'''



#TODO: add support for exporting and importing data to/from csv
import requests
import argparse
from sys import argv, exit

parser = argparse.ArgumentParser()
parser.add_argument("callsign", help='the callsign to search')
parser.add_argument('--name', help='licensee name', action='store_true')
parser.add_argument('--address', help='licensee address', action='store_true')
parser.add_argument('--expiration', help='license expiration date', action='store_true')
parser.add_argument('--status', help='license status', action='store_true')
parser.add_argument('--class', help='license class', action='store_true')
args = parser.parse_args()

url = "http://api.hamdb.org/{}/json/PorkPy"

r = requests.get(url.format(args.callsign))

hamdb_response = r.json()['hamdb']

if hamdb_response['messages']['status'] == 'NOT_FOUND':
    print("\nCallsign Not Found\n")
    exit()

callsign_info = hamdb_response['callsign']
call = callsign_info['call']
full_name = "{0} {1} {2}".format(callsign_info['fname'], callsign_info['mi'], callsign_info['name']).strip()
grid = callsign_info['grid']
license_class = callsign_info['class']
country = callsign_info['country']
addr1 = callsign_info['addr1']
city  = callsign_info['addr2']
state  = callsign_info['state']
zcode  = callsign_info['zip']
status = callsign_info['status']
expiration = callsign_info['expires']

response = """
              CALLSIGN:    {0}
              CLASS:       {3}
              NAME:        {1}
              GRID:        {2}
              ADDRESS:     {4}
                           {5}
                           {6}, {7} {8}
"""


if args.address:
   print( """
            ADDRESS: {0}
                     {1}
                     {2}, {3} {4}
    """.format(country, addr1, city, state, zcode))
if args.name:
    print("""
            NAME: {}
    """.format(full_name))
else:
    print(response.format(call, full_name, grid, license_class, country,addr1, city, state, zcode))

