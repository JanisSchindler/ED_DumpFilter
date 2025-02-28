# ED_DumpFilter

This command line script takes a zipped systems.*.json.gz from https://www.spansh.co.uk/dumps and filters it based on the distance to a reference systems coordinates.

Requirements
Python 3.13.2
orjson

usage: src/main.py [-h] [--maxDistance MAXDISTANCE] [--origin ORIGIN] path

where
--maxDistance is the distance to check for. The default is 1500 LY
--origin is the reference system given by its coordinates in x|y|z. The default is Sol (0|0|0)
path is the path to the zip file

Example

src/main.py --origin '5000|1000|10000' --maxDistance 2000 systems_1month.json.gz