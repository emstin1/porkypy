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




import requests
from sys import argv, exit
#TODO: use argparse for easier ooptions

callsign = argv[1]
url = "http://api.hamdb.org/{}/json/PorkPy"

r = requests.get(url.format(callsign))

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

response = """
              CALLSIGN:    {0}
              CLASS:       {3}
              NAME:        {1}
              GRID:        {2}
              ADDRESS:     {4}
                           {5}
                           {6}, {7} {8}
"""
print(response.format(call, full_name, grid, license_class, country,addr1, city, state, zcode))
